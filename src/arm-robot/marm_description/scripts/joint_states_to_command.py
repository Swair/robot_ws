#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

# 定义关节的命令发布器
joint_pubs = []

def joint_states_callback(msg):
    # 将收到的 joint_states 数据转换为各个关节的控制命令并发布
    if len(msg.position) >= 6:  # 确保有至少6个关节数据
        joint_pubs[0].publish(msg.position[0])  # joint1
        joint_pubs[1].publish(msg.position[1])  # joint2
        joint_pubs[2].publish(msg.position[2])  # joint3
        joint_pubs[3].publish(msg.position[3])  # joint4
        joint_pubs[4].publish(msg.position[4])  # joint5
        joint_pubs[5].publish(msg.position[5])  # joint6

def main():
    global joint_pubs

    rospy.init_node('joint_states_to_command', anonymous=True)

    # 创建发布器，将关节位置发布到对应的控制器话题
    joint_pubs = [
        rospy.Publisher('/arm/joint1_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/arm/joint2_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/arm/joint3_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/arm/joint4_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/arm/joint5_position_controller/command', Float64, queue_size=10),
        rospy.Publisher('/arm/joint6_position_controller/command', Float64, queue_size=10)
    ]

    # 订阅 /arm/joint_states 话题
    rospy.Subscriber("/joint_states", JointState, joint_states_callback)

    # 保持节点运行
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
