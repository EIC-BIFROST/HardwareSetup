```
https://github.com/mavlink/mavros/blob/ros2/mavros/README.md#installation
```
Find Pixhawk /dev/serial
```
ls /dev/serial/by-id/usb-Auterion_PX4_FMU_v6X.x_0-if00 
```
Start extract Data from Pixhawk
```
ros2 launch mavros px4.launch fcu_url:=serial:///dev/serial/by-id/usb-Auterion_PX4_FMU_v6X.x_0-if00:115200
```
the command below is suck cause the port can change so don't use it just keep in mind that we can use it
```
ros2 launch mavros px4.launch fcu_url:=serial:///dev/ttyACM0:115200
```
echo the imu topic
```
ros2 topic echo /mavros/imu/data
```
