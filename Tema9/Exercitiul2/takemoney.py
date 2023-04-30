from interfaces import State, Observable


class DisplayObserver:
    def update(self, amount: int):
        print(f'The Vending Machine now has {amount / 100} lei')


class TakeMoneySTM(Observable):
    current_state: State
    money: int = 0

    def __init__(self):
        super().__init__()

        self.attach(DisplayObserver())

        self.wait_state = WaitingForClient()
        self.wait_state.state_machine = self

        self.insert_money_state = InsertMoney()
        self.insert_money_state.state_machine = self

        self.current_state = self.wait_state

    def add_money(self, value: int):
        self.money += value
        self.notify_all(argument=self.money)

    def update_amount_of_money(self, value: int):
        self.money = value
        self.notify_all(argument=self.money)


class WaitingForClient(State):
    state_machine: TakeMoneySTM

    def client_arrived(self):
        self.state_machine.current_state = self.state_machine.insert_money_state


class InsertMoney(State):
    state_machine: TakeMoneySTM

    def insert_10bani(self):
        self.state_machine.add_money(10)

    def insert_50bani(self):
        self.state_machine.add_money(50)

    def insert_1leu(self):
        self.state_machine.add_money(100)

    def insert_5lei(self):
        self.state_machine.add_money(500)

    def insert_10lei(self):
        self.state_machine.add_money(1000)
