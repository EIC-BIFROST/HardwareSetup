from typing import Literal
from pymavlink import mavutil
master = mavutil.mavlink_connection('udp:127.0.0.1:14552')

def check_RC_value(functionName: Literal['payloadDrop', 'CVSim', 'chan9_raw', 'chan10_raw']):
    msg = master.recv_match(type='RC_CHANNELS', blocking=False)
    if msg is None:
        return False, 0
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
    print(position)
    return True, position
'''
while True:
    valid, position = check_RC_value('payloadDrop')
    if valid:
        print(valid, position)
'''