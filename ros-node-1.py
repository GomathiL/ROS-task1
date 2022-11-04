#!usr/bin/env python 
import rospy
from std_msgs.msg import String, Int32, Float32
import random

def randTemp():
    return random.randint(32,212)

def talker():
    pub = rospy.Publisher('farenheit', Int32, queue_size=10)
    rospy.init_node('ros-node-1', anonymous=True)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        tempValues = randTemp()
        rospy.loginfo(tempValues)
        pub.publish(tempValues)
        rate.sleep() 
  
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass