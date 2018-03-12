from easingutilities.easing.BackEase import BackEase
from easingutilities.easing.BounceEase import BounceEase
from easingutilities.easing.BounceEaseOut import BounceEaseOut
from easingutilities.easing.CircularBounceEase import CircularBounceEase
from easingutilities.easing.CircularEase import CircularEase
from easingutilities.easing.CubicEase import CubicEase
from easingutilities.easing.ExponentialEase import ExponentialEase
from easingutilities.easing.LinearEase import LinearEase
from easingutilities.easing.QuadraticEase import QuadraticEase
from easingutilities.easing.QuarticEase import QuarticEase
from easingutilities.easing.QuinticEase import QuinticEase
from easingutilities.easing.SinusoidalEase import SinusoidalEase

easing = CircularBounceEase()

for number in range(1, 2000):
    ease_factor = easing.calculate_next_step(number, 1, 1, 2000)
    if number % 20 is 0:
        print(ease_factor)



