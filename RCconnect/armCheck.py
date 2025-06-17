from mavsdk import System
import asyncio

async def check_arm_status():
    drone = System()
    await drone.connect(system_address="udp://:14551")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    while True:
        async for armed in drone.telemetry.armed():
            print(f"Is armed: {armed}")
            break
        if armed:
            break


if __name__ == "__main__":
    asyncio.run(check_arm_status())