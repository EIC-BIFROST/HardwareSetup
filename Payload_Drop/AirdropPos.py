import asyncio
import time
import RanGenCoor
import RCreadChannel

position = 0

def simCV():
    start = time.time() 
    time_limit = 2  # seconds
    global position
    while True:
        valid, position = RCreadChannel.check_RC_value('CVSim')
        if valid:
            # print(position)
            if time.time() - start > time_limit:
                print("Time limit reached, randomizing position")
                Inp = False
                latCV = 0
                longCV = 0
                break
            if position > 0:
                Inp = True
                latCV = 38.314552
                longCV = -76.552369
                break
    return Inp, latCV, longCV

async def main(runway):
    #Assigning the air drop position
    Inp, latCV, longCV = simCV()
    if Inp == True:
        lat, long = latCV, longCV
    if Inp == False:
        # Random the coordinate 
        lat, long = RanGenCoor.main(runway, 1)
    print(Inp, lat, long)
    return lat, long
    

#asyncio.run(main(1))