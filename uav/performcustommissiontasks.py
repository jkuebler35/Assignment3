#!/usr/bin/env python

import rospy
import smach
import time
from random import randint

# define state PerformCustomMissionTasks
class PerformCustomMissionTasks(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['additional_tasks','recalled'])
        self.counter = 0

    def execute(self, userdata):
     	time.sleep(1)
        value = randint(1,10)
        rospy.loginfo('Value is %s', value)
        if (value > 5):
            rospy.loginfo('UAV recalled')
            return 'recalled'
        else:
            rospy.loginfo('Additional mission tasks assigned')
            return 'additional_tasks'
