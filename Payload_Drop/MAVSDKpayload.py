import asyncio
from mavsdk import System
import RCreadChannel
import time


DropHeight = 10
ServoTime = 8 #servo dropping state
#'''
#tuning by time constant (ServoTime) with RC interrupt
async def autoDrop(drone, t):
    start = time.time()
    print(start)
    print("Start air dropping process")
    await drone.action.set_actuator(1, 0)
    while time.time() - start < t:
        valid, position = RCreadChannel.check_RC_value('payloadDrop')
        if valid and position == 1:
            print('Goodbye')
            break
        #'''
        await asyncio.sleep(0.1)
    await drone.action.set_actuator(1, 1)
    await asyncio.sleep(1)
    await drone.action.set_actuator(1, -1)
    print("air drop done")
#'''
#100% Manual Drop 
async def ManualDrop(drone):
    print("Start air dropping process")
    while True:
        valid, position = RCreadChannel.check_RC_value('payloadDrop') #use SD switch on RC to control
        if valid:
            if position == -1:
                await drone.action.set_actuator(1, -1)
                print('not dropping')
            if position == 0:
                await drone.action.set_actuator(1, 0)
                print('dropping')
            if position == 1:
                await drone.action.set_actuator(1, 1)
                print('Goodbye')
                await asyncio.sleep(1)
                break
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
    '''
    # If want to test with out take off, take line 65-70 and line 74-76 out but the drone will operate only 6 second.
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        print(health.is_global_position_ok, health.is_home_position_ok)
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break
    #'''
    await drone.action.arm()
    print("Armed")
    await drone.action.set_actuator(1, -1)
    #await drone.action.set_takeoff_altitude(DropHeight)
    #await drone.action.takeoff()
    #print("Takeoff")
    #await ManualDrop(drone)
    await autoDrop(drone, ServoTime)
    #await drone.action.land()
    #print("Landing")
    await drone.action.disarm()
    print("Disarmed")
    
    
if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
