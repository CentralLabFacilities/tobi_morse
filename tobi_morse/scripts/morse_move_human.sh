#!/bin/bash

source /opt/ros/kinetic/setup.bash

rostopic pub /morse/human/motion  geometry_msgs/Twist "linear:
  x: 0.0
  y: 5
  z: 0.0
angular:
  x: 0.0
  y: 1.0
  z: 1.0"
