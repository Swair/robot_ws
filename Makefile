PACKAGE_NAME := robot_ws
PROJECT_DIR := ${shell pwd}
BUILD_DIR   := ${PROJECT_DIR}/build
INSTALL_DIR := ${BUILD_DIR}/install
NUM_JOB := 4
GIT_COMMIT_HASH = ${shell cd ${PROJECT_DIR} && git log -1 --format=%h --abbrev=8}
PACKAGE_VERSION := v1.0.0-${GIT_COMMIT_HASH}
CMAKE := cmake

# BUILD_TYPE ?= Release
BUILD_TYPE := Debug

CMAKE_ARGS := \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DTIMEOUT_REPLY_CONFIG=ON \
        -DCMAKE_BUILD_TYPE=${BUILD_TYPE}


######################## build ########################
build:
	catkin_make -DCATKIN_WHITELIST_PACKAGES="" ${PROJECT_DIR}
.PHONY: build

clean:
	rm -rf ${BUILD_DIR}	
.PHONY: clean

######################## docker ########################
build_images:
	cd tool/docker && \
	docker build -t ros_image_dev:1.0.0 .
.PHONY: build_images

dev_in_docker:
	docker run -it --name u20ros --privileged --net=host -v /tmp/.X11-unix:/tmp/.X11-unix -v ${PROJECT_DIR}:${PROJECT_DIR} -p 11111:22 ros_image_dev:1.0.0 /bin/bash
.PHONY: dev_in_docker
# docker builder prune

dev_in_u20ros:
	docker start u20ros && \
	docker exec -it u20ros /bin/bash
.PHONY: dev_in_ros

clear_u20ros:
	docker rm u20ros -f
.PHONY: clear_dev


######################## run ########################

## https://github.com/Liuyvjin/shixi_dual_ur?tab=readme-ov-file
demo:
	roslaunch dual_ur_moveit_config demo.launch
.PHONY: demo


