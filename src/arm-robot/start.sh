#!/bin/bash

# 确保脚本在失败时停止
set -e

# 源代码环境
source ~/catkin_test/devel/setup.bash

# 启动 Gazebo
roslaunch robot_moveit_config gazebo.launch &

# 等待 Gazebo 启动
sleep 15  # 根据需要调整等待时间

# 启动 joint_state_publisher_gui
rosrun joint_state_publisher_gui joint_state_publisher_gui &

# 启动 joint_states_to_command.py
rosrun marm_description joint_states_to_command.py &

sleep 1

rosrun marm_description states_to_positions.py &

sleep 1

rosrun rosserial_python serial_node.py /dev/ttyUSB0 

