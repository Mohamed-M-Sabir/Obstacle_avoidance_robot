#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
#import serial
#arduinoData=serial.Serial("/dev/ttyACM0",9600)

velocity_linear=0
velocity_angular=0
def callback(data):
    global velocity_linear
    global velocity_angular
    
    twist = Twist()
    left_stick_up_down=data.axes[1]
    left_stick_left_right=data.axes[0]
    right_stick_up_down=data.axes[4]
    right_stick_left_right=data.axes[3]
     

    x=data.axes[6]
    y=data.axes[7]
    Max=180
    Min=1
  
    if(x==1):
        velocity_linear+=1
        x=velocity_linear
        if(velocity_linear>=180):
            velocity_linear=Max
    elif(x==-1):
        velocity_linear-=1
        if(velocity_linear<=1):
            velocity_linear=Min



    if(y==1):
        velocity_angular+=1
        y=velocity_angular
        if(velocity_angular>=180):
            velocity_angular=Max
    elif(y==-1):
        velocity_angular-=1
        if(velocity_angular<=1):
            velocity_angular=Min 


    twist.linear.x=right_stick_up_down
    twist.angular.z=left_stick_left_right                                    
    
    
        


    #z=arduinoData.write(format(twist.linear.x))
    #print(z)
    rospy.loginfo('velocity_linear=%s',velocity_linear)
    rospy.loginfo('velocity_angular=%s',velocity_angular)
    #twist.angular.z = 4*data.axes[0]
    pub.publish(twist)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('cmd_vel', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Turtle')
    rospy.spin()

if __name__ == '__main__':
    start()
