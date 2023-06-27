from colega import Colega
from student import Student

if __name__ == '__main__':
    panciuc = Student('Panciuc')
    colega = Colega('Radu')

    colega.get_together_with(panciuc)
    colega.ignore(panciuc)
    colega.break_up_with(panciuc)