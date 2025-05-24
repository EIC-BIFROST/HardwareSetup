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

## 🚀 Installation

### 1. Install MAVROS for ROS 2 Humble

Follow the official MAVROS installation instructions:  
🔗 [Official MAVROS README (ROS 2)](https://github.com/mavlink/mavros/blob/ros2/mavros/README.md#installation)

Install the packages:
```bash
sudo apt install ros-humble-mavros ros-humble-mavros-extras
