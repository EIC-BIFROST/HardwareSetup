from mavsdk import System
import asyncio

async def get_float_param_names(drone):
    # Get all parameters
    all_params = await drone.param.get_all_params()
    
    # Extract names of float parameters
    float_param_names = [param.name for param in all_params.float_params]
    
    return float_param_names

# Usage example
async def main():
    drone = System()
    await drone.connect(system_address="udp://:14551")
    print("Connected to the drone")
    
    # Get float parameter names
    float_param_names = await get_float_param_names(drone)
    print("Available float parameters:", float_param_names)
    
    # Now you can use these names with get_param_float
    if float_param_names:
        param_name = float_param_names[0]
        param_value = await drone.param.get_param_float(param_name)
        print(f"Parameter {param_name} value: {param_value}")

if __name__ == "__main__":
    asyncio.run(main())