# STD Imports
import numpy as np
import sys
import cv2
from Queue import Queue

# RSB Specifics
import rsb
import rst
from rsb.converter import registerGlobalConverter
from rstconverters import Cv2ImageConverter

# ROS Specifics
import rospy
import roslib
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class ROSImage:
    def __init__(self, rsb_publisher):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/morse/tobi/rgb_cam/image", Image, self.callback)
        self.rsb_publisher = rsb_publisher

    def callback(self, data):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(data, "passthrough")
            # cv_2_img = cv2.cv.CreateImageHeader((cv_img.shape[1], cv_img.shape[0]), cv2.cv.IPL_DEPTH_8U, 3)
            # cv2.cv.SetData(ipl_i, cv_img.tostring(), cv_img.dtype.itemsize * 3 * cv_img.shape[1])
            self.rsb_publisher.pub(cv_img)
            # print ">>> Publishing"
        except CvBridgeError as e:
            print e


class RSBPublisher():
    def __init__(self):
        self.informer = rsb.createInformer(str(sys.argv[1]), dataType=np.ndarray)

    def pub(self, data):
        self.informer.publishData(data)


if __name__ == "__main__":
    rospy.init_node('MORSE2RSBIMAGE', anonymous=True)
    registerGlobalConverter(Cv2ImageConverter())
    rsb_p = RSBPublisher()
    ros_s = ROSImage(rsb_p)
    print ">>> Publishing MORSE image to %s: " % sys.argv[1]
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

