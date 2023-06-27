from enum import Enum



class StudentState(Enum):
    HAPPY = 1
    DESPERATE = 2
    SAD = 3  # :(

class Student:
    state: StudentState = StudentState.HAPPY
    name: str

    def __init__(self, name):
        self.name = name

    def set_state(self, state: StudentState):
        self.state = state
        print(f'{self.name} is now {self.state}')

