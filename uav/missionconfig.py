#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state MissionConfig
class MissionConfig(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['config_completed'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The configuration is complete')
     	time.sleep(1)
      	return 'config_completed'
