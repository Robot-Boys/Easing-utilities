import math

from easingutilities.easing.AbstractEase import AbstractEase


class CircularEase(AbstractEase):

    # Stolen from: https://gist.github.com/th0ma5w/9883420
    @classmethod
    def calculate_next_step(self, current_step, start_value, change_in_value, number_of_steps):
        current_step /= number_of_steps / 2
        if current_step < 1:
            return -change_in_value / 2 * (math.sqrt(1 - current_step * current_step) - 1) + start_value
        current_step -= 2
        return change_in_value / 2 * (math.sqrt(1 - current_step * current_step) + 1) + start_value
