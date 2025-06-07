import asyncio
import time
from pymavlink import mavutil
import RanGenCoor
from typing import Literal

def check_RC_value(functionName: Literal['payloadDrop', 'CVSim', 'chan9_raw', 'chan10_raw']):
    master = mavutil.mavlink_connection('udp:127.0.0.1:14552')
    msg = master.recv_match(type='RC_CHANNELS', blocking=True)
    channel_map = {
        'payloadDrop': msg.chan8_raw, 
        'CVSim': msg.chan7_raw, 
        'chan9_raw': msg.chan9_raw, 
        'chan10_raw': msg.chan10_raw}
    funcVal = channel_map[functionName]
    if funcVal < 1000:
        position = -1 # normal drop
    elif funcVal < 1500:
        position = 0 # stop
    else:
        position = 1 # fast drop
    return position

def simCV():
    start = time.time() 
    time_limit = 5  # seconds
    while True:
        print(check_RC_value('CVSim'))
        if time.time() - start > time_limit:
            print("Time limit reached, breaking loop.")
            Inp = False
            latCV = 0
            longCV = 0
            break
        if check_RC_value('CVSim') > 0:
            Inp = True
            latCV = 38.314552
            longCV = -76.552369
            break
    return Inp, latCV, longCV

   
async def main(runway):
    Inp, latCV, longCV = simCV()
    if Inp == True:
        print(latCV, longCV)
    if Inp == False:
        # Random the coordinate 
        lat, long = RanGenCoor.main(runway, 1)
        print(lat, long)

asyncio.run(main(1))