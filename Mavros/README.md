# MAVROS with Jetson Orin Nano (Jetson Linux 36.4.3)

This guide explains how to set up MAVROS (ROS 2 Humble) on a Jetson Orin Nano with Jetson Linux 36.4.3 to interface with a Pixhawk flight controller over USB.

## ⚙️ Hardware Requirements

- **Jetson Orin Nano** (Jetson Linux 36.4.3)
- **Pixhawk** flight controller (tested with FMUv6X)
- **USB-C to USB-A cable**

## 🔌 **Important Note**:  
Use a **USB-C to USB-A** cable to connect the **Pixhawk USB-C port** to the **Jetson Orin Nano USB-A port**.  
Jetson Orin Nano’s USB-C port cannot be used for communication in this setup because it's not in the correct USB mode.

---


### 1. Install MAVROS for ROS 2 Humble

Follow the official MAVROS installation instructions:  
🔗 [Official MAVROS README (ROS 2)](https://github.com/mavlink/mavros/blob/ros2/mavros/README.md#installation)

Install the packages:
```bash
sudo apt install ros-humble-mavros ros-humble-mavros-extras
````




### 2. Identify the Pixhawk Serial Port

After plugging in the Pixhawk via USB, list the device under `/dev/serial/by-id`:

```bash
ls /dev/serial/by-id/usb-Auterion_PX4_FMU_v6X.x_0-if00
```

You should see a path like:

```
/dev/serial/by-id/usb-Auterion_PX4_FMU_v6X.x_0-if00
```

This path is symlinked and **more stable** than using `/dev/ttyACM0` (which may change across reboots).




### 3. Start MAVROS with the Correct FCU URL

Use the symlinked serial path in the `fcu_url`:

```bash
ros2 launch mavros px4.launch fcu_url:=serial:///dev/serial/by-id/usb-Auterion_PX4_FMU_v6X.x_0-if00:115200
```

⚠️ **Avoid using `/dev/ttyACM0`**:
Although this might work, the port can change and cause instability. For example:

```bash
# This method is not recommended:
ros2 launch mavros px4.launch fcu_url:=serial:///dev/ttyACM0:115200
```




### 4. Echo IMU Data

Once MAVROS is running, check if data is being received from the Pixhawk:

```bash
ros2 topic echo /mavros/imu/data
```

If everything is set up correctly, you will see streaming IMU data.

---

## ✅ Summary

* Install `ros-humble-mavros` and `mavros-extras`
* Use a **USB-C to USB-A** cable (Jetson USB-A port only)
* Always use `/dev/serial/by-id/...` instead of `/dev/ttyACM*`
* Verify with `/mavros/imu/data` topic


