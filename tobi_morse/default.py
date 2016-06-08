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
scan.properties(Visible_arc=False)
scan.properties(laser_range=9.0)
scan.properties(resolution=1.0)
scan.properties(scan_window=180.0)
scan.create_laser_arc()
scan.frequency(40.0)
scan.add_stream("ros", topic="/scan")
tobi.append(scan)

# A differential drive actuator
motion = MotionVWDiff()
motion.properties(ControlType='Position')
tobi.append(motion)
motion.add_interface("ros", topic="/cmd_vel")

# Video Camera
videocamera = VideoCamera()
videocamera.translate(0.0, -0.10, 1.35)
videocamera.properties(cam_width=640, cam_height=480, cam_focal=35.0, capturing=True, Vertical_Flip=True)
tobi.append(videocamera)
videocamera.add_interface("ros", topic="/morse/rgb_cam/")

# Adding a waypoint Actuator
waypoint_human = Waypoint('waypoint_human')
waypoint_human.properties(ObstacleAvoidance=False, ControlType="Position")

# Adding a Pose sensor
pose_human = Pose('pose_human')

# Adding Orientation
orientation_human = Orientation('orientation_human')

# orientation_human.add_stream('socket')
orientation_human.add_service('socket')
# pose_human.add_stream('socket')
pose_human.add_service('socket')
# waypoint_human.add_stream('socket')
waypoint_human.add_service('socket')

# A human avatar
human = Human()
human.translate(x=2.0, y=-2.2, z=0.0)
human.append(waypoint_human)
human.append(pose_human)
human.append(orientation_human)

# Control The Human with a Keyboard
keyboard = Keyboard()
human.append(keyboard)

# Set the environment
env = Environment('test', fastmode=False)
# env = Environment('indoors-1/indoor-1')
# env.add_service('socket')


