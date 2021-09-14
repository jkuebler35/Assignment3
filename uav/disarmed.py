#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state Disarmed
class Disarmed(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_stop'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('UAV has been disarmed')
     	time.sleep(1)
        return 'do_stop'
