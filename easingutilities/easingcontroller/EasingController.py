# Can generate positions for a motor
# Uses python 3. iteration protocol
# see: https://docs.python.org/3/c-api/iter.html
from enum import Enum

from easingutilities.easing.CircularEase import CircularEase
from easingutilities.easing.CubicEase import CubicEase
from easingutilities.easing.ExponentialEase import ExponentialEase
from easingutilities.easing.LinearEase import LinearEase
from easingutilities.easing.QuadraticEase import QuadraticEase
from easingutilities.easing.QuarticEase import QuarticEase
from easingutilities.easing.QuinticEase import QuinticEase
from easingutilities.easing.SinusoidalEase import SinusoidalEase
from easingutilities.exceptions.ControllerNotConfiguredException import ControllerNotConfiguredException
from easingutilities.exceptions.WrongMovementException import WrongMovementException


class EasingType(Enum):
    LINEAR = 0
    SINE = 1
    CUBIC = 2
    QUADRATIC = 3
    QUARTIC = 4
    QUINTIC = 5
    EXPONENTIAL = 6
    CIRCULAR = 7


class EasingController(object):
    def __init__(self, motor, movement_type=EasingType.LINEAR, iterations=2000):
        self._motor = motor
        self._iterations = iterations
        self.easing = self.choose_easing(movement_type)
        self._goal = None
        self._move_direction = None

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        if goal > 90:
            self._goal = 90
        elif goal < -90:
            self._goal = -90
        else:
            self._goal = goal

        self._move_direction = self.calculate_move_direction(self._goal)

        print("Goal set to: ", self._goal)

    def __iter__(self):
        self.check_if_ready()
        self._current_step = 0
        self._start_position = self._motor.present_position
        self._distance_to_travel = self.calculate_distance(self._motor.present_position, self._goal)
        return self

    def __next__(self):
        self._current_step += 1
        if self._current_step > self._iterations:
            raise StopIteration
        ease_factor = self.easing.calculate_next_step(self._current_step, 0, 1, self._iterations)
        ease_move = ease_factor * self._distance_to_travel
        return self._start_position + ease_move * self._move_direction

    @staticmethod
    def calculate_distance(first, second):
        return abs(first - second)
        # According to stack overflow this works:
        # https://stackoverflow.com/questions/13602170/how-do-i-find-the-difference-between-two-values-without-knowing-which-is-larger

    @staticmethod
    def calculate_move_direction(goal):
        if goal < 0:
            return -1
        else:
            return 1

    def check_if_ready(self):
        if self._goal is None:
            raise ControllerNotConfiguredException("You should provide a goal before using this")

    @staticmethod
    def choose_easing(self, movement_type):
        if movement_type is EasingType.LINEAR:
            return LinearEase()
        elif movement_type is EasingType.SINE:
            return SinusoidalEase()
        elif movement_type is EasingType.CUBIC:
            return CubicEase()
        elif movement_type is EasingType.QUADRATIC:
            return QuadraticEase()
        elif movement_type is EasingType.QUARTIC:
            return QuarticEase()
        elif movement_type is EasingType.QUINTIC:
            return QuinticEase()
        elif movement_type is EasingType.EXPONENTIAL:
            return ExponentialEase()
        elif movement_type is EasingType.CIRCULAR:
            return CircularEase()
        else:
            raise WrongMovementException("The movement type specified does not exist")
