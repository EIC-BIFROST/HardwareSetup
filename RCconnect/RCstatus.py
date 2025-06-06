from mavsdk import System
from mavsdk.telemetry import Telemetry
import asyncio

async def get_rc_status(drone: System):
    telemetry = Telemetry(drone)
    async for rc_status in telemetry.subscribe_rc_status():
        print("RC status:")
        print(f"  Was available once: {rc_status.was_available_once}")
        print(f"  Is available: {rc_status.is_available}")
        print(f"  Signal strength: {rc_status.signal_strength_percent}")

async def main():
    drone = System()
    await drone.connect(system_address="udp://:14551")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    await get_rc_status(drone)

if __name__ == "__main__":
    asyncio.run(main())