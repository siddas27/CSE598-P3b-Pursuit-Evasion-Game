#!/usr/bin/env python
from __future__ import print_function
import roslib
from std_msgs.msg import Int8
import time

roslib.load_manifest('pursuit_evasion')
import sys
import rospy
from geometry_msgs.msg import Twist
from darknet_ros_msgs.msg import BoundingBoxes, ObjectCount


class DetectionInfo:

    def __init__(self):
        self.pub = rospy.Publisher('tb3_0/cmd_vel', Twist, queue_size=1)

        self.image_sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, self.callback_follow)
        self.found_sub = rospy.Subscriber("/darknet_ros/found_object", ObjectCount, self.callback_detected)
        self.c_diff = 0
        self.detected = 0

    def callback_detected(self, data):
        if data.count == 1:
            self.detected = 1
        else:
            self.detected = 0

    def callback_follow(self, data):
        xmin = data.bounding_boxes[0].xmin
        xmax = data.bounding_boxes[0].xmax
        object_center = (xmax + xmin) / 2
        image_center = 320
        self.c_diff = image_center - object_center


def main(args):
    di = DetectionInfo()
    rospy.init_node('detection_info', anonymous=True)
    start_time = time.time()
    move = Twist()
    while not rospy.is_shutdown():
        print(di.c_diff, di.detected)
        if di.detected:
            if di.c_diff > 30:
                move.linear.x = 0
                # adjust orientation
                move.angular.z = 0.001 * di.c_diff
                di.pub.publish(move)
                rospy.sleep(1)
		move.linear.x = 0.25
                # adjust orientation
                move.angular.z = 0.0
                di.pub.publish(move)
                rospy.sleep(2)
            else:
                move.linear.x = 0.25
                # adjust orientation
                move.angular.z = 0.0
                di.pub.publish(move)
                rospy.sleep(2)

        else:
            move.linear.x = 0
            move.linear.y = 0.0
            move.angular.z = 0.2
            di.pub.publish(move)
            rospy.sleep(0.5)

        # stop after 5mins
        current_time = time.time()
        if current_time - start_time > 5 * 60:
            break


if __name__ == '__main__':
    main(sys.argv)
