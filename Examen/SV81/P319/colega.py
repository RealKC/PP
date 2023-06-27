from student import Student
from commands import MakeSad, MakeDesperate, MakeHappy

class Colega(Student):
    def __init__(self, name: str):
        super().__init__(name)

    def ignore(self, other):
        MakeDesperate().execute(other)

    def break_up_with(self, other):
        MakeSad().execute(other)

    def get_together_with(self, other):
        MakeHappy().execute(other)