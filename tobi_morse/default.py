from morse.builder import *

# Add the TOBI robot
tobi = PatrolBot()

# Add a clock for simulation time
clock = Clock()
tobi.append(clock)
clock.add_interface('ros', topic="/clock")

# Add an odometry sensor
odometry = Odometry()
tobi.append(odometry)
odometry.add_stream("ros", topic="/odom")

# A Sick laser scanner
scan = Sick()
scan.translate(x=0.05, y=0.0, z=0.1)
scan.properties(Visible_arc = True)
scan.properties(laser_range = 9.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()
scan.frequency(40.0)
scan.add_stream("ros", topic="/base_scan")
tobi.append(scan)

# A differential drive actuator
motion = MotionVWDiff()
motion.properties(ControlType='Position')
tobi.append(motion)
motion.add_interface("ros", topic="/cmd_vel")

# A human avatar
human = Human()
human.translate(x=2.0, y=-2.2, z=0.0)
human_motion = Waypoint()
human_motion.properties(ControlType="Position")
human.append(human_motion)
human_motion.add_interface("ros", topic="/human_pose")

# Control The Human with a Keyboard
keyboard = Keyboard()
human.append(keyboard)

# Set the environment
env = Environment('test', fastmode=False)
# env = Environment('indoors-1/indoor-1')


