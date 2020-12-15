#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
def callback(data):
    range=round(data.range*10)
    rospy.loginfo('range=%s',range)
    twist=Twist()
    if range>2:
        twist.linear.x=-1
    elif range<=2:
        twist.angular.z=1
        if range<=2:
            twist.angular.z=-1
    pub.publish(twist)        

    


if __name__ == "__main__":
    global pub
    rospy.init_node("ultrasonic")
    rospy.Subscriber("/rangeSonar",Range,callback)
    pub = rospy.Publisher('cmd_vel', Twist)
    rospy.spin()