from morse.builder import *

tobi = Pioneer3DX()
#tobi = PatrolBot()
# tobi = Tobi()
# tobi.translate(x=2.0, y=-2.0, z=0.00)
# tobi.translate(x=2.0, y=0.0, z=-0.02)

clock = Clock()
tobi.append(clock)
clock.add_interface('ros', topic="/clock")

#keyboard = Keyboard()
#tobi.append(keyboard)

odometry = Odometry()
tobi.append(odometry)
odometry.add_stream("ros", topic="/odom")

pose = Pose()
tobi.append(pose)

scan = Sick()
scan.translate(x=0.05, y=0.0, z=0.051)
scan.properties(Visible_arc = True)
scan.properties(laser_range = 9.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.frequency(40.0)
scan.add_stream("ros", topic="/base_scan")
tobi.append(scan)

motion = MotionVWDiff()
motion.properties(ControlType='Position')
tobi.append(motion)
motion.add_interface("ros", topic="/cmd_vel")

human = Human()
human.translate(x=2.0, y=-2.2, z=0.0)
human_motion = Waypoint()
human_motion.properties(ControlType="Position")
human.append(human_motion)
human_motion.add_stream('socket')

#env = Environment('tum_kitchen/tum_kitchen', fastmode=False)
env = Environment('indoors-1/indoor-1', fastmode=False)
#env = Environment('test', fastmode=False)
#env = Environment('laas/grande_salle', fastmode=False)
#env = Environment('apartment', fastmode=False)
#env = Environment('outdoors', fastmode=False)
#env.set_camera_rotation([1.0470, 0, 5.7854])
#env.set_camera_location([-12.0, -16.0, 10.0])
