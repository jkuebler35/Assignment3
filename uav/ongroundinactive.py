#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state OnGroundInactive
class OnGroundInactive(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['preflight_checks_initiated'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The preflight checks are initiated')
     	time.sleep(1)
      	return 'preflight_checks_initiated'
