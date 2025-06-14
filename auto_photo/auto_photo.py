import asyncio
from mavsdk import System
import cv2
import utm
import math

waypoints = [
    (38.3158934, -76.5495924, 25),  # Location 1
    (38.3162740, -76.5518748, 25),  # Location 2
    (38.3157330, -76.5516235, 25)   # Location 3
]

visited = set()

THRESHOLD_METERS = 3  # Distance tolerance

def capture_image(filename):
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    if ret:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        cv2.imwrite(filename, frame)
        print(f"✅ Saved image: {filename}")
    else:
        print("❌ Failed to capture image")
    cap.release()

async def run():
    # Init the drone
    drone = System()


    await drone.connect(system_address="udp://:14540")

    print("🔄 Waiting for GPS fix...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("✅ GPS OK")
            break

    print("📍 Monitoring location to trigger captures...")
    asyncio.ensure_future(check_position_in_waypoint(drone))

    while True:
        await asyncio.sleep(0.1)

async def check_position_in_waypoint(drone):
    async for position in drone.telemetry.position():
        for i, (target_lat, target_lon, targer_alt) in enumerate(waypoints):
            if i in visited:
                continue

            distance = cal_distance(position.latitude_deg,position.longitude_deg,position.relative_altitude_m,target_lat,target_lon,targer_alt)
            if distance < THRESHOLD_METERS:
                print(f"🎯 Reached waypoint {i+1}: {target_lat}, {target_lon}, {targer_alt}m (Distance: {distance:.2f} m)")
                filename = f"image_wp{i+1}_{target_lat:.5f}_{target_lon:.5f}.jpg"
                capture_image(filename)
                visited.add(i)

        if len(visited) == len(waypoints):
            print("✅ All waypoints captured. Exiting.")
            break


def cal_distance(lat1, lon1, alt1, lat2, lon2, alt2):
    northing1,easting1,_,_ = utm.from_latlon(lat1,lon1)
    northing2,easting2,_,_ = utm.from_latlon(lat2,lon2)
    dx = easting2 - easting1
    dy = northing2 - northing1
    dz = alt2 - alt1
    return math.sqrt(dx**2 + dy**2 + dz**2)

if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
