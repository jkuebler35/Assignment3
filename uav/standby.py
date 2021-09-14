#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state Preflght Checks
class Standby(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['launch_command_received'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Launch command recieved')
     	time.sleep(1)
        return 'launch_command_received'
