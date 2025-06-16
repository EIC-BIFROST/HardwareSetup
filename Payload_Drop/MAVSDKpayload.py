import asyncio
from mavsdk import System
import RCreadChannel
import time


DropHeight = 10
ServoTime = 6 #servo dropping state

#tuning by time constant (ServoTime) with RC interrupt
async def autoDrop(drone, ind, t):
    for i in range(4): #depends on the number of servo on drone
        await drone.action.set_actuator(i+1, -1)
    halfValue = [0.4, 0.1, 0.1, 0] #dropping state tunning-required parameter
    start = time.time()
    print("Start air dropping process")
    await drone.action.set_actuator(ind, halfValue[ind-1])
    while time.time() - start < t:
        if RCreadChannel.check_RC_value('payload')[1] == 1 and RCreadChannel.check_RC_value('payload')[0]:
            print('Goodbye')
            break
        await asyncio.sleep(0.1)
    await drone.action.set_actuator(ind, 1)
    await asyncio.sleep(1)
    await drone.action.set_actuator(ind, -1)
    print("air drop done")

#100% Manual Drop 
async def ManualDrop(drone, ind):
    for i in range(4): #depends on the number of servo on drone
        await drone.action.set_actuator(i+1, -1)
    halfValue = [0.4, 0.1, 0.1, 0] #dropping state tunning-required parameter probably 0
    print("Start air dropping process")
    while True:
        valid, position = RCreadChannel.check_RC_value('payload') #use SD switch on RC to control
        if valid:
            if position == -1:
                await drone.action.set_actuator(ind, -1)
                print('not dropping')
            if position == 0:
                await drone.action.set_actuator(ind, halfValue[ind-1])
                print('dropping')
            if position == 1:
                await drone.action.set_actuator(ind, 1)
                print('Goodbye')
                await asyncio.sleep(1)
                break
        await asyncio.sleep(0.1)
    print("air drop done")
        
async def run():

    #initial drone connection
    print("program run")
    drone = System()
    #await drone.connect(system_address = "serial:///dev/serial/by-id/usb-FTDI_FT231X_USB_UART_D30IKJWG-if00-port0:57600")
    await drone.connect(system_address= "udp://:14551")
    print("Drone connection process started!")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    # If want to test with out take off, take line 65-70 and line 74-76 out but the drone will operate only 6 second.
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        print(health.is_global_position_ok, health.is_home_position_ok)
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break
    
    await drone.action.arm()
    print("Armed")
    await drone.action.set_takeoff_altitude(DropHeight)
    await drone.action.takeoff()
    print("Takeoff")
    await ManualDrop(drone, 1) # means using AUX1 to control the servo from pixhawk (Peripheral actuator set1 on QGC)
    await drone.action.land()
    print("Landing")
    await drone.action.disarm()
    print("Disarmed")
    
    
if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
