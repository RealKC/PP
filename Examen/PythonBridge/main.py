from abc import ABC, abstractmethod


class MamiferImplementor(ABC):
    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def interact_with_impl(self, other):
        raise NotImplementedError(f'MamiferImplementor: not implemented {self.__class__.__name__}')


def decorate_impl(replaced):
    def decorator(func):
        def interact(this, other):
            if replaced(this, other) is not None:
                func(this, other)

        return interact
    return decorator


class Mamifer:
    implementation: MamiferImplementor

    def __init__(self, impl: MamiferImplementor):
        self.implementation = impl

    def interact_with(self, other):
        self.implementation.interact_with_impl(other.implementation)


class Femeie(MamiferImplementor):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with_impl(self, other):
        print(f'Sunt femeie si interactionez cu {other}')


class Pisica(MamiferImplementor):
    def interact_with_impl(self, other):
        print('Miauuu')


class Caine(MamiferImplementor):
    def interact_with_impl(self, other):
        print('Ham ham')


class Om(MamiferImplementor):
    @decorate_impl(lambda this, other: print(f'Hai la suc {other}') if isinstance(other, Femeie) else False)
    def interact_with_impl(self, other):
        print(f'Sunt barbat si interactionez cu {other}')


if __name__ == '__main__':
    barbat = Mamifer(Om())
    femeie = Mamifer(Femeie('Roxana'))
    fifi = Mamifer(Pisica())
    panciuc = Mamifer(Caine())

    barbat.interact_with(femeie)
    barbat.interact_with(fifi)
    fifi.interact_with(femeie)
    femeie.interact_with(panciuc)
    panciuc.interact_with(femeie)
