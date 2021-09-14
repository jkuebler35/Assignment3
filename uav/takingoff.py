#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state TakingOff
class TakingOff(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['altitude_reached','takeoff_aborted'])
        self.counter = 0

    def execute(self, userdata):
     	time.sleep(1)
        value = randint(1,10)
        rospy.loginfo('Value is %s', value)
        if (value > 5):
            rospy.loginfo('Altitude reached')
            return 'altitude_reached'
        else:
            rospy.loginfo('Takeoff aborted')
            return 'takeoff_aborted'
