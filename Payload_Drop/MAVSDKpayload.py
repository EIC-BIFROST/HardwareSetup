import asyncio
from mavsdk import System

async def run():

    #initial drone connection
    print("program run")
    drone = System()
    await drone.connect(system_address = "serial:///dev/ttyUSB0:57600")
    #serial:///dev/serial/by-id/usb-FTDI_FT231X_USB_UART_D30IKJWG-if00-port0:57600
    #udp://:14540
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
    await drone.action.set_actuator(1, 0)
    print("servo moved")
    
    
if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
