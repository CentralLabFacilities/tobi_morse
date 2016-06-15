#!/bin/bash

source /opt/ros/indigo/setup.bash
rosbag record $* --output-name=$WORKSPACE/follow-me-fast