#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
import mavros

def gps_callback(data):
	rospy.loginfo(data.latitude)

def gps_listener():
    
    rospy.init_node('gps_router', anonymous=True)
    rospy.Subscriber("drone1_gps", NavSatFix, gps_callback)

    rospy.spin()


if __name__ == '__main__':
	gps_listener()
