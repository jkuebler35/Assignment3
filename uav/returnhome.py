#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state ReturnHome
class ReturnHome(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['reached_home_coordinates'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('UAV reached home coordinates')
     	time.sleep(1)
        return 'reached_home_coordinates'
