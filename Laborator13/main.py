import types
from typing import *
from functools import reduce
from math import sqrt
from functional import seq
from functional.util import unpack


### Exercitiul 1 ###

def aop_simulation(before, after, replace=None):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            if isinstance(before, types.FunctionType):
                before()  # execute before function
            if replace and isinstance(replace, types.FunctionType):
                output = replace(*args, **kwargs)
            else:
                output = f(*args, **kwargs)
            if isinstance(after, types.FunctionType):
                after()  # execute after function
            return output
        return wrapped_f
    return wrap


def is_prime(n: int):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for d in range(3, int(sqrt(n)), 2):
        if n % d == 0:
            return False

    return True


class int(int):
    @aop_simulation(before=lambda: print('Before'), after=lambda: print('After'), replace=is_prime)
    def is_prime(self) -> bool:
        return False


### Exercitiul 2 ###
class str(str):
    def to_pascal_case(self):
        split = self.split(" ")
        mapped = map(lambda s: s[0].upper() + s[1:], split)
        return reduce(lambda acc, s: acc + s, mapped)


### Exercitiul 3 ###
T = TypeVar('T')
U = TypeVar('U')


def fake_zip(a: List[T], b: List[U]) -> Iterable[Tuple[T, U]]:
    return map(lambda tup: (tup[1], b[tup[0]]), enumerate(a))


### Exercitiul 4 ###

def is_perfect_square(n: int) -> bool:
    return sqrt(n) == int(sqrt(n))


def print_perfect_squares(n: int):
    perfect_squares = filter(is_perfect_square, (x for x in range(n)))

    print(f'The perfect squares in the interval [0, {n}] are: ')
    for perf_square in perfect_squares:
        print(perf_square, end=' ')
    print()


if __name__ == "__main__":
    # Exercitiul 1
    print(f'3 is prime? {int(3).is_prime()}')

    # Exercitiul 2
    print(str("Hello world").to_pascal_case())

    # Exercitiul 3
    a = [1, 2, 3]
    b = [4, 5, 6]
    zipped = fake_zip(a, b)
    for thing in zipped:
        print(thing)

    # Exercitiul 4
    print_perfect_squares(17)

    # Exercitiul 5
    string = input('Give me a string: ')
    distinct = seq(list(string)).distinct().reduce(lambda acc, x: acc + x, '')
    print(distinct)
