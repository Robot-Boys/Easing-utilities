# Very simple driver to test EasingController emulated the behasvior of a primitive
import time

from utilities.config.MotorTester import MotorTester
from utilities.easingcontroller.EasingController import EasingController


class Driver(object):
    def __init__(self):
        self._stop = False
        self._motor1_controller = EasingController(1000)
        self.tester = MotorTester()
        self.tester.scan_ports()
        self.robot = self.tester.test_robot()
        self.robot.start_sync()
        self.tester.reset_robot(self.robot)

    def make_movement(self):
        print("Make Movement")
        movement = {}
        for n in EasingController(70):
            self.robot.m4.goal_position = n
            time.sleep(0.2 )
