from morse.builder import *# Add the TOBI robottobi = PatrolBot()tobi.translate(x=-0.5, y=0.0, z=0.0)# Add a Clock for simulation timeclock = Clock()clock.add_interface('ros', topic="/clock")tobi.append(clock)# Add an Odometry sensorodometry = Odometry()odometry.frequency(10.0)odometry.add_stream("ros", topic="/odom")tobi.append(odometry)# A Sick laser scannerscan = Sick()scan.translate(x=0.05, y=0.0, z=0.1)scan.properties(Visible_arc=False)scan.properties(laser_range=9.0)scan.properties(resolution=0.5)scan.properties(scan_window=180.0)scan.create_laser_arc()scan.frequency(30.0)scan.add_stream("ros", topic="/scan")scan.add_stream("ros", topic="/scan_merged")tobi.append(scan)# A Differential Drive actuatormotion = MotionVWDiff()motion.properties(ControlType='Position')motion.add_interface("ros", topic="/cmd_vel")motion.frequency(10.0)tobi.append(motion)# Video Cameravideocamera = VideoCamera()videocamera.translate(0.0, -0.10, 1.35)videocamera.properties(cam_width=640, cam_height=480, cam_focal=35.0, capturing=True, Vertical_Flip=True)videocamera.frequency(15.0)videocamera.add_interface("ros", topic="/morse/tobi/rgb_cam/")tobi.append(videocamera)# Adding a waypoint Actuatorwaypoint_human = Waypoint('waypoint_human')waypoint_human.properties(ObstacleAvoidance=True, ControlType="Position")waypoint_human.add_stream('socket')waypoint_human.add_service('socket')# Creates a new instance of the actuatormotionxyw = MotionXYW()tobi.append(motionxyw)motionxyw.add_interface("ros", topic="/morse/human/motion")# Adding a Pose sensorpose_human = Pose('pose_human')pose_human.add_stream('socket')pose_human.frequency(1.0)pose_human.add_interface('ros', topic="/morse/human/pose", frame_id='human')# Adding a Pose sensorpose_robot = Pose('pose_robot')pose_robot.frequency(1.0)pose_robot.add_interface('ros', topic="/morse/tobi/pose", frame_id='tobi')tobi.append(pose_robot)# A human avatarhuman = Human()human.translate(x=0.5, y=0.0, z=0.0)human.rotate(0.0, 0.0, 3.1)human.append(waypoint_human)human.append(pose_human)human.append(motionxyw)# Control The Human with a Keyboardkeyboard = Keyboard()human.append(keyboard)# Set the environment# env = Environment('empty', fastmode=False)# env = Environment('indoors-1/boxes', fastmode=False)env = Environment('test')# env.add_service('socket')