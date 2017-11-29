from easingutilities.easing.AbstractEase import AbstractEase

#Demo of how to use the strategy pattern to mix easing strategies
from easingutilities.easing.BounceEase import BounceEase
from easingutilities.easing.CircularEase import CircularEase


class LinearEase(AbstractEase):
    @classmethod
    def calculate_next_step(cls, current_step, start_value, change_in_value, number_of_steps):
        progress = LinearEase().calculate_next_step(current_step, start_value, change_in_value, number_of_steps)
        if progress < 0.5:
            return CircularEase().calculate_next_step(current_step, start_value, change_in_value, number_of_steps)
        else:
            return BounceEase().calculate_next_step(current_step, start_value, change_in_value, number_of_steps)



