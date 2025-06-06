from pymavlink import mavutil
import asyncio

async def check_RC_value(indy):
    master = mavutil.mavlink_connection('udp:127.0.0.1:14552')
    msg = master.recv_match(type='RC_CHANNELS', blocking=True)
    channel_map = [msg.chan7_raw, msg.chan8_raw, msg.chan9_raw, msg.chan10_raw]
    result = {}
    for j in range(4):
        if channel_map[j] < 1000:
            result[j +1] = "not dropped"
        elif channel_map[j] < 1500:
            result[j +1] = "dropping"
        else:
            result[j+1] = "dropped"
    print(result[indy])

if __name__ == "__main__":
    # Run the asyncio loop
    while True:
        asyncio.run(check_RC_value(4))