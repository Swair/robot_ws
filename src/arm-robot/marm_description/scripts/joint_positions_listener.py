#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def joint_positions_callback(msg):
    # 打印收到的关节位置
    rospy.loginfo("Received joint positions: %s", msg.data)

def main():
    rospy.init_node('joint_positions_listener', anonymous=True)

    # 订阅 /joint_positions 话题
    rospy.Subscriber("/joint_positions", Float64MultiArray, joint_positions_callback)

    # 保持节点运行
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
