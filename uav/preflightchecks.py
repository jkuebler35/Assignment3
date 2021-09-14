#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state Preflght Checks
class PreflightChecks(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['preflight_checks_failed','preflight_checks_passed'])
        self.counter = 0

    def execute(self, userdata):
     	time.sleep(1)
        value = randint(1,10)
        rospy.loginfo('Value is %s', value)
        if (value > 5):
            rospy.loginfo('Preflight checks passed')
            return 'preflight_checks_passed'
        else:
            rospy.loginfo('Preflight checks failed')
            return 'preflight_checks_failed'
