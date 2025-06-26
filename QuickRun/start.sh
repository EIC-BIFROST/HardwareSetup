#!/bin/bash

tmux new-session -d -s drone_session

# Window 1: MAVLink router
tmux rename-window -t drone_session 'MAVLink'
tmux send-keys -t drone_session \
  'mavlink-routerd -e 127.0.0.1:14551 -e 127.0.0.1:14552 /dev/serial/by-path/platform-3610000.usb-usb-0\:2.3\:1.0:57600' C-m

# Window 2: Docker Python execution
tmux split-window -h -t drone_session
tmux send-keys -t drone_session \
  'docker start eic && docker exec -it eic bash -c "cd /workspace/home/jetson/Autonomous_Drone && python3 run.py; exec bash"' C-m

# Optional: layout
tmux select-layout -t drone_session tiled

# Attach to tmux session
tmux attach-session -t drone_session
