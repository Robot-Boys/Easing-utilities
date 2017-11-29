class AbstractEase(object):

    @classmethod
    def calculate_next_step(self, current_step, start_value, change_in_value, number_of_steps):
        raise  ("You should have implemented this")

