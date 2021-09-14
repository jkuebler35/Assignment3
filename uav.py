#!/usr/bin/env python

import rospy
import smach
import time
from random import randint
from uav.missionconfig import MissionConfig
from uav.ongroundinactive import OnGroundInactive
from uav.preflightchecks import PreflightChecks
from uav.standby import Standby
from uav.arming import Arming
from uav.takingoff import TakingOff
from uav.performcustommissiontasks import PerformCustomMissionTasks
from uav.returnhome import ReturnHome
from uav.land import Land
from uav.disarmed import Disarmed

# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The UAV has been disarmed')
	    time.sleep(1)
        return 'do_exit'

# main
def main():

    rospy.init_node('UAV')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('MissionConfig', MissionConfig(),
                               transitions={'config_completed':'OnGroundInactive'})
        smach.StateMachine.add('OnGroundInactive', OnGroundInactive(),
                                transitions={'preflight_checks_initiated':'PreflightChecks'})
        smach.StateMachine.add('PreflightChecks', PreflightChecks(),
                               transitions={'preflight_checks_failed':'OnGroundInactive','preflight_checks_passed':'Standby'})
        smach.StateMachine.add('Standby', Standby(),
                               transitions={'launch_command_received':'Arming'})
        smach.StateMachine.add('Arming', Arming(),
                               transitions={'arming_failed':'OnGroundInactive','armed':'TakingOff'})
        smach.StateMachine.add('TakingOff', TakingOff(),
                               transitions={'altitude_reached':'PerformCustomMissionTasks','takeoff_aborted':'Land'})
        smach.StateMachine.add('PerformCustomMission', PerformCustomMissionTasks(),
                               transitions={'additional_tasks':'PerformCustomMission','recalled':'ReturnHome'})
        smach.StateMachine.add('ReturnHome', ReturnHome(),
                               transitions={'reached_home_coordinates':'Land'})
        smach.StateMachine.add('Land', Land(),
                               transitions={'landed':'Disarmed'})
        smach.StateMachine.add('Disarmed', Disarmed(),
                               transitions={'do_stop':'Stop'})
        smach.StateMachine.add('Stop', Stop(),
                               transitions={'do_exit':'do_exit'})


    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
