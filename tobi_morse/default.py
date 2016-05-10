from morse.builder import *

tobi = Pioneer3DX()
tobi.translate(x=0.5, y=0.2, z=0.0)

clock = Clock()
tobi.append(clock)
clock.add_interface('ros', topic="/clock")

keyboard = Keyboard()
tobi.append(keyboard)

odometry = Odometry()
tobi.append(odometry)
odometry.add_stream("ros", topic="/odom")

pose = Pose()
tobi.append(pose)

scan = Sick()
scan.translate(x=0.06, y=0.0, z=0.1)
tobi.append(scan)
scan.properties(Visible_arc = True)
scan.properties(laser_range = 7.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.add_stream("ros", topic="/base_scan")

motion = MotionVWDiff()
motion.properties(ControlType='Position')
tobi.append(motion)
motion.add_interface("ros", topic="/cmd_vel")

env = Environment('laas/grande_salle')
env.set_camera_rotation([1.0470, 0, 0.7854])