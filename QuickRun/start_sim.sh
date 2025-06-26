#!/bin/bash

tmux new-session -d -s drone_session

# Window 1: MAVLink router
tmux rename-window -t drone_session 'MAVLink'
tmux send-keys -t drone_session \
  'mavlink-routerd -e 10.0.0.120:14550 127.0.0.1:14550' C-m

# Window 2: Docker Python execution
tmux split-window -h -t drone_session
tmux send-keys -t drone_session \
  'docker start eic && docker exec -it eic bash -c "cd /workspace/home/jetson/Autonomous_Drone && python3 run.py -s; exec bash"' C-m

# Window 3: PX4 SITL simulation inside Docker
tmux split-window -v -t drone_session
tmux send-keys -t drone_session \
  'docker exec -it eic bash -c "cd /workspace/home/jetson/PX4-Autopilot && make px4_sitl gz_x500; exec bash"' C-m

# Layout & attach
tmux select-layout -t drone_session tiled
tmux attach-session -t drone_session

