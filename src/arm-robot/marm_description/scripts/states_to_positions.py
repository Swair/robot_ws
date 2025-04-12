#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray,Float32MultiArray

SERVOMIN = 150  # 最小脉冲长度
SERVOMAX = 600  # 最大脉冲长度

def map_value(value, in_min, in_max, out_min, out_max):
    # 将输入值从一个范围映射到另一个范围
    return out_min + (out_max - out_min) * (value - in_min) / (in_max - in_min)

def joint_states_callback(msg):
    # 创建一个新的消息来发布关节位置
    position_msg = Float32MultiArray()
    
    # 将关节位置从弧度转换为PWM值
    position_msg.data = [
        int(map_value(round(pos, 7), 0, 3.1415926, SERVOMIN, SERVOMAX)) 
        for pos in msg.position[:7]  # 只取前7个关节的位置
    ]

    # 发布到新的话题
    joint_positions_pub.publish(position_msg)

if __name__ == '__main__':
    rospy.init_node('states_test')  # 初始化节点

    # 订阅 /joint_states 话题
    rospy.Subscriber('/joint_states', JointState, joint_states_callback)

    # 创建一个发布者，发布到 /joint_positions 话题
    joint_positions_pub = rospy.Publisher('/joint_positions', Float32MultiArray, queue_size=10)

    rospy.loginfo("states_test node is running, publishing joint positions...")
    rate = rospy.Rate(10)  # 设置频率为 10 Hz

    # 循环等待回调
    #rospy.spin()
    while not rospy.is_shutdown():
        # 循环等待回调
        rate.sleep()

