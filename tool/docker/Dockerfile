FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i "s/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/us.archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/security.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.tuna.tsinghua.edu.cn\/debian-security/g" /etc/apt/sources.list
RUN sed -i "s/httpredir.debian.org/mirrors.tuna.tsinghua.edu.cn\/debian-security/g" /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y xfce4 xfce4-goodies
RUN apt-get install -y net-tools openssh-server byobu curl wget tar sudo htop man unzip ca-certificates pkg-config
RUN apt-get install -y build-essential autoconf software-properties-common libtool yasm make cmake g++ vim ctags cscope git 
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libx11-dev libxrandr-dev libxkbcommon-x11-0 libgl1-mesa-glx libgl1-mesa-dev mesa-utils

RUN sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
RUN gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    gpg --export --armor C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 > /etc/apt/trusted.gpg.d/ros-archive-keyring.asc
RUN apt-get update
RUN apt install -y ros-noetic-desktop-full

####### dependence ############
RUN apt-get install -y ros-noetic-industrial-msgs
RUN apt-get install -y ros-noetic-serial
RUN apt-get install -y ros-noetic-ur-msgs
RUN apt-get install -y ros-noetic-moveit ros-noetic-rviz-visual-tools ros-noetic-moveit-visual-tools ros-noetic-franka-description

RUN apt-get install -y python3-yaml python3-rospkg



EXPOSE 22

ARG MyUser=docker
RUN useradd --create-home ${MyUser} 
RUN adduser ${MyUser} sudo 
RUN echo "${MyUser}:12345" | chpasswd
RUN echo "root:12345" | chpasswd

ENV LANG C.UTF-8
ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1
ENV LIBGL_ALWAYS_SOFTWARE=1
ENV ROS_DISTRO=noetic
ENV ROS_PACKAGE_PATH=/opt/ros/noetic/share
ENV ROS_ROOT=/opt/ros/noetic/share/ros
ENV ROS_ETC_DIR=/opt/ros/noetic/etc/ros
ENV ROSLISP_PACKAGE_DIRECTORIES=/home/ros/catkin_ws/devel/share/common-lisp
ENV ROS_PYTHON_VERSION=3

WORKDIR /home/${MyUser}
ENV HOME /home/${MyUser}
ADD .bashrc /home/${MyUser}/.bashrc
RUN chown ${MyUser} /home/${MyUser} -R
RUN chgrp ${MyUser} /home/${MyUser} -R
USER ${MyUser}
CMD ["bash"]

WORKDIR /home/WRshares/robot_ws



