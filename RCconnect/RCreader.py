#!/usr/bin/env python3

import asyncio
from mavsdk import System

async def read_rc_map_aux1(drone):
    try:
        # Get the RC_MAP_AUX1 parameter value
        rc_map_aux1 = await drone.param.get_param_float("RC7_MIN")
        print(f"RC_MAP_AUX1 value: {rc_map_aux1}")
        return rc_map_aux1
    except Exception as e:
        print(f"Failed to get RC_MAP_AUX1: {e}")
        return None

async def main():
    # Connect to the drone
    drone = System()
    await drone.connect(system_address="udp://:14551")
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    # Read the RC_MAP_AUX1 parameter
    await read_rc_map_aux1(drone)

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(main())