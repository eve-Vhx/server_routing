#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
import mavros
import random


def gps_publisher():
    rospy.init_node('fake_gps_data', anonymous=True)
    gps_pub = rospy.Publisher('drone1_gps', NavSatFix, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        gps_data = NavSatFix()
        gps_data.latitude = random.uniform(10.1, 12.1)
        gps_data.longitude = random.uniform(10.1, 12.1)
        gps_data.altitude = random.uniform(10.1, 12.1)

        gps_pub.publish(gps_data)
        rate.sleep()

if __name__ == '__main__':
    try:
        gps_publisher()

    except rospy.ROSInterruptException:
        pass