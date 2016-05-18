# STD Imports
import cv2
from Queue import Queue

# RSB Specifics
import rsb
import rst
import rstsandbox
from rsb.converter import registerGlobalConverter
from rstconverters.opencv import IplimageConverter

# ROS Specifics
import rospy
import roslib
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class ROSImage:
    def __init__(self, rsb_publisher):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/morse/rgb_cam/image", Image, self.callback)
        self.rsb_publisher = rsb_publisher

    def callback(self, data):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            ipl_i = cv2.cv.CreateImageHeader((cv_img.shape[1], cv_img.shape[0]), cv2.cv.IPL_DEPTH_8U, 3)
            cv2.cv.SetData(ipl_i, cv_img.tostring(), cv_img.dtype.itemsize * 3 * cv_img.shape[1])
            self.rsb_publisher.pub(ipl_i)
            print ">>> Publishing"
        except CvBridgeError as e:
            print e


class RSBPublisher():
    def __init__(self):
        self.informer = rsb.createInformer("/video", dataType=cv2.cv.iplimage)

    def pub(self, data):
        self.informer.publishData(data)


if __name__ == "__main__":
    rospy.init_node('MORSE2RSBIMAGE', anonymous=True)
    registerGlobalConverter(IplimageConverter())
    rsb_p = RSBPublisher()
    ros_s = ROSImage(rsb_p)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")