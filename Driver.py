# Very simple driver to test EasingController emulated the behasvior of a primitive
import time

from config.MotorTester import MotorTester
from easingutilities.easingcontroller.EasingController import EasingController, EasingType


class Driver(object):
    def __init__(self):
        self._stop = False
        self.tester = MotorTester()
        self.tester.scan_ports()
        self.robot = self.tester.test_robot()
        self.robot.start_sync()
        self.tester.reset_robot(self.robot)

    def move_first(self):

        motor = self.robot.m4
        controller = EasingController(motor, EasingType.CUBIC)
        controller.goal = -50
        for move in controller:
            motor.goal_position = move
            time.sleep(0.002)
        else:
            print("Move done")

        controller.goal = 50

        time.sleep(5)

        # todo: debug this
        for move in controller:
            motor.goal_position = move
            time.sleep(0.002)

    def make_movement(self):
        print("Make Movement")
        self.controllers = self.config_controller_test_array()
        while True:
            try:
                self.move_motors_one_step()
            except StopIteration:
                break
        else:
            print("Loop Stopped")

    def move_motors_one_step(self):
        position = {}
        for motor in self.robot.motors:
            key = motor.name
            try:
                controller = self.controllers[key]
                pos = controller.__next__()
                position[key] = pos
                self.robot.goto_position(position, 0.002, None, True)
            except StopIteration:
                raise StopIteration

    def config_controller_test_array(self):
        res = {}
        for motor in self.robot.motors:
            key = motor.name
            controller = EasingController(motor)
            controller.goal = 70
            controller.__iter__()
            res[key] = controller

        return res
