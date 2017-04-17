#!/bin/bash

source /opt/ros/kinetic/setup.bash

rostopic pub /morse/human/motion  geometry_msgs/Twist "linear:
  x: 1
  y: 0.5
  z: 0.0
angular:
  x: 0.0
  y: 0.5
  z: 0.5"
