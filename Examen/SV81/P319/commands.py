from abc import abstractmethod, ABC
from student import Student, StudentState


class Command(ABC):
    @abstractmethod
    def execute(self, student: Student):
        raise NotImplementedError('pure virtual function')


class MakeDesperate(Command):
    def execute(self, student: Student):
        student.set_state(StudentState.DESPERATE)

class MakeSad(Command):
    def execute(self, student: Student):
        student.set_state(StudentState.SAD)


class MakeHappy(Command):
    def execute(self, student: Student):
        student.set_state(StudentState.HAPPY)
