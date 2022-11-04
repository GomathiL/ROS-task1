#!usr/bin/env python 
import rospy
from from std_msgs.msg import String, Int32, Float32

def callback(data):
    rospy.Publisher(data.data)
    
def listener():
    rospy.init_node('ros-node-3', anonymous=True)
    rospy.Subscriber('celsius', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()