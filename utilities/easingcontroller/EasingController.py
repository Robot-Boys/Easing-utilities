# Can generate positions for a motor
# Uses python 3. iteration protocol
# see: https://docs.python.org/3/c-api/iter.html

class EasingController(object):
    def __init__(self, goal):
        self.goal = goal

    def __iter__(self):
        self.current_step = 0
        return self

    def __next__(self):
        self.current_step += 1
        if self.current_step > self.goal:
            raise StopIteration
        return self.current_step
