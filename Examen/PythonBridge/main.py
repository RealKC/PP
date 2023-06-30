from abc import ABC, abstractmethod


class MamiferImplementor(ABC):
    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def interact_with_impl(self, other):
        raise NotImplementedError(f'MamiferImplementor: not implemented {self.__class__.__name__}')


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
    def interact_with_impl(self, other):
        if isinstance(other, Femeie):
            print(f'Buna {other}, vrei sa iesim la o cafea?')
        elif isinstance(other, Pisica):
            print(f'Ce pisica draguta!')
        else:
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
