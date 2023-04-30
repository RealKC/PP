from abc import ABC, abstractmethod
from interfaces import State, Observable


class ChoiceObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class SelectProductsSTM(Observable):
    current_state: State

    def __init__(self):
        super().__init__()

        self.select_products_state = SelectProduct()
        self.select_products_state.state_machine = self

        self.coca_cola_state = CocaCola()
        self.coca_cola_state.state_machine = self

        self.pepsi_state = Pepsi()
        self.pepsi_state.state_machine = self

        self.sprite_state = Sprite()
        self.sprite_state.state_machine = self

        self.current_state = self.select_products_state

    def choose_another_product(self):
        self.current_state = self.select_products_state
        self.current_state.choose()
        self.notify_all()


class SelectProduct(State):
    state_machine: SelectProductsSTM
    price: float = 0.0

    def choose(self):
        print('Alegeti o optiune: ')
        print(f'\t1) Coca-Cola ({self.state_machine.coca_cola_state.price} RON)')
        print(f'\t2) Pepsi ({self.state_machine.pepsi_state.price}) RON')
        print(f'\t3) Sprite ({self.state_machine.sprite_state.price}) RON')

        choice = int(input('Alegerea dvs.: '))

        match choice:
            case 1:
                self.state_machine.current_state = self.state_machine.coca_cola_state
            case 2:
                self.state_machine.current_state = self.state_machine.pepsi_state
            case 3:
                self.state_machine.current_state = self.state_machine.sprite_state


class CocaCola(State):
    state_machine: SelectProductsSTM
    price: float = 5.5


class Pepsi(State):
    state_machine: SelectProductsSTM
    price: float = 5.40


class Sprite(State):
    state_machine: SelectProductsSTM
    price: float = 5
