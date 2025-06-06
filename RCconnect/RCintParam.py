from mavsdk import System
import asyncio

async def get_int_param_names(drone):
    # Get all parameters
    all_params = await drone.param.get_all_params()
    
    # Extract names of integer parameters
    int_param_names = [param.name for param in all_params.int_params]
    
    return int_param_names

# Usage example
async def main():
    drone = System()
    await drone.connect(system_address="udp://:14551")
    print("Connected to the drone")
    
    # Get integer parameter names
    int_param_names = await get_int_param_names(drone)
    print("Available integer parameters:", int_param_names)
    
    # Now you can use these names with get_param_int
    if int_param_names:
        param_name = int_param_names[0]
        param_value = await drone.param.get_param_int(param_name)
        print(f"Parameter {param_name} value: {param_value}")

if __name__ == "__main__":
    asyncio.run(main())