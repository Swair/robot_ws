#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg
import sys  # 添加这一行导入 sys 模块

def move_panda_arm():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('panda_moveit_node', anonymous=True)

    # robot = moveit_commander.RobotCommander()
    group = moveit_commander.MoveGroupCommander("panda_arm")

    pose_target = geometry_msgs.msg.Pose()
    pose_target.position.x = 0.2
    pose_target.position.y = 0.2
    pose_target.position.z = 0.5
    pose_target.orientation.w = 1.0

    group.set_pose_target(pose_target)

    plan = group.go(wait=True)
    group.stop()
    group.clear_pose_targets()

    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_panda_arm()
    except rospy.ROSInterruptException:
        pass