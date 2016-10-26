#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from sensor_msgs.msg import LaserScan

# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim or any other robot

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):

    twist = Twist()
    twist.linear.x = 4*data.axes[1]
    twist.angular.z = 4*data.axes[0]
    pub.publish(twist)

 def callback1(data):
 	LaserScan = LaserScan()
 	for i in range(240,480):
 		if LaserScan.ranges[i] <= 2:
 			threshold = False

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('cmd_vel', Twist,queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    rospy.Subscriber("hokuyo_scan", LaserScan, callback1)
    # starts the node
    rospy.init_node('Joy2Turtle')
    rospy.spin()

if __name__ == '__main__':
    start()
