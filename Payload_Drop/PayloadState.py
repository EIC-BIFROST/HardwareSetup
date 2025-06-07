import asyncio
from mavsdk import System
from pymavlink import mavutil

# just for sim
CV_detected = True

def check_RC_value():
    master = mavutil.mavlink_connection('udp:127.0.0.1:14552')
    msg = master.recv_match(type='RC_CHANNELS', blocking=True)
    if msg.chan7_raw < 1000:
        speed = 0.5 # normal drop
    elif msg.chan7_raw < 1500:
        speed = 0 # stop
    else:
        speed = 1 # fast drop
    return speed

async def Start_dropping():
    if CV_detected == True:
        pos = [cv_x, cv_y]
        drop_function(pos)
        return True
    else:
        if CV_detected == True:
            pos = [cv_x, cv_y, cv_z]
            drop_function(pos)
        else:
            random_drop()
        return False


async def main():
    
    speed = await check_RC_value()
    print(speed)
    await asyncio.sleep(1)