#!usr/bin/env python 
import rospy
from from std_msgs.msg import String, Int32, Float32

def convTemp(f):
    c = (f-32)*(5/9)
    return c

def callback(data):
    c = convTemp(data.data)
    pub = rospy.Publisher('celsius', Float32, queue_size=10)
    rospy.loginfo(c)
    pub.publish(c)
    
def listener():
    rospy.init_node('ros-node-2', anonymous=True)
    rospy.Subscriber('farenheit', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()