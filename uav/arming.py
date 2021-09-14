#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state Arming
class Arming(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['armed','arming_failed'])
        self.counter = 0

    def execute(self, userdata):
     	time.sleep(1)
        value = randint(1,10)
        rospy.loginfo('Value is %s', value)
        if (value > 5):
            rospy.loginfo('UAV armed')
            return 'armed'
        else:
            rospy.loginfo('UAV arming failed')
            return 'arming_failed'
