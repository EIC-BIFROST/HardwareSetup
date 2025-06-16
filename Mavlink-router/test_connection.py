#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System()
    await drone.connect(system_address="serial:///dev/serial/by-id/usb-FTDI_FT231X_USB_UART_D30IKJWG-if00-port0:57600")

    status_text_task = asyncio.ensure_future(print_status_text(drone))

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    #End the loop    
    status_text_task.cancel()


async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
