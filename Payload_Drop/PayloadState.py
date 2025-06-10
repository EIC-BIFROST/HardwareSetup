import asyncio
from mavsdk import System
import AirdropPos
import RCreadChannel

drone = System()
runway = 1
ind = 1


async def Start_dropping():
    await drone.connect(system_address="udp://:14551")
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    
    await drone.action.arm()
    #lat, long = await AirdropPos.main(runway)
    D = 0
    print(D)
    while D < 16:
        valid, position = RCreadChannel.check_RC_value('payloadDrop')
        if valid:
            if position == -1:
                await drone.action.set_actuator(ind, 0)
                await asyncio.sleep(0.5)
                await drone.action.set_actuator(ind, -1)
                await asyncio.sleep(0.1)
                D += 1.225
                print('normal drop')
            elif position == 0:
                await drone.action.set_actuator(ind, -1)
                await asyncio.sleep(0.1)
                print('stop drop')
            elif position == 1:
                await drone.action.set_actuator(ind, 0)
                await asyncio.sleep(4)
                print('goodbye')
                break
        print(D)
    print('air drop done')

asyncio.run(Start_dropping())