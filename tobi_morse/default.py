from morse.builder import *

# Append ToBi
tobi = PatrolBot()
tobi.add_interface('ros')

odometry = Odometry()
tobi.append(odometry)
odometry.add_interface('ros', topic="/odom")

keyboard = Keyboard()
tobi.append(keyboard)

scan = Sick()
scan.translate(x=0.275, z=0.252)
tobi.append(scan)
scan.properties(Visible_arc = True)
scan.properties(laser_range = 9.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.add_interface('ros', topic='/scan', frame_id='base_link')

motion = MotionVWDiff()
motion.properties(ControlType = 'Position')
tobi.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

env = Environment('indoors-1/indoor-1')
