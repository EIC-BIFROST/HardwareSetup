import asyncio
from mavsdk import System

async def drop(drone, ind, t):
    for i in range(4):
        await drone.action.set_actuator(i+1, -1)
    halfValue = [0.4, 0.1, 0.1, 0]
    print("Start air dropping process")
    await drone.action.set_actuator(ind, halfValue[ind-1])
    await asyncio.sleep(t)
    await drone.action.set_actuator(ind, 1)
    await asyncio.sleep(1)
    await drone.action.set_actuator(ind, -1)
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
    # print("Waiting for drone to have a global position estimate...")
    # async for health in drone.telemetry.health():
    #     print(health.is_global_position_ok, health.is_home_position_ok)
    #     if health.is_global_position_ok and health.is_home_position_ok:
    #         print("-- Global position estimate OK")
    #         break
    
    await drone.action.arm()
    print("Armed")
    await drop(drone, 1, 1)
    await drop(drone, 4, 1)
    print("servo moved")
    
    
if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
