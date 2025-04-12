#!/bin/bash
xacro arm.xacro > arm.urdf
check_urdf arm.urdf
