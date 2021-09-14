#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state Land
class Land(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['landed'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('UAV has landed')
     	time.sleep(1)
        return 'landed'

