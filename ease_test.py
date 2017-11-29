from easingutilities.easing.CubicEase import CubicEase
from easingutilities.easing.LinearEase import LinearEase
from easingutilities.easing.SinEase import SinEase

easing = CubicEase()

for number in range(0, 2000):
    ease_factor = easing.calculate_next_step(number, 1, 1, 2000)
    print(ease_factor)



