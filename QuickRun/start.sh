#!/bin/bash

# Run MAVLink Router (cleaned up: removed invalid command)
echo "Starting MAVLink Router..."
mavlink-routerd -e 127.0.0.1:14550 -e 127.0.0.1:14551 -e 127.0.0.1:14552 /dev/serial/by-id/usb-Auterion_PX4_v6X.x_0-if00:57600 &

# Optional: wait for mavlink-routerd to initialize
sleep 4

# Start the Docker container
echo "Starting Docker container 'eic'..."
docker start eic

# Attach to the container
echo "Attaching to Docker container..."
docker attach eic

# After detaching from Docker (Ctrl+P + Ctrl+Q), continue
echo "Continuing after Docker..."

cd workspace/home/jetson/Autonomous_Drone || {
    echo "Directory not found!"
    exit 1
}

# Run the Python script
echo "Running run.py..."
python3 run.py
