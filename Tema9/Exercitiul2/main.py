from selectproducts import SelectProductsSTM, ChoiceObserver
from takemoney import TakeMoneySTM


class VendingMachineSTM(ChoiceObserver):
    take_money_stm: TakeMoneySTM
    select_products_stm: SelectProductsSTM

    def __init__(self):
        self.take_money_stm = TakeMoneySTM()
        self.select_products_stm = SelectProductsSTM()
        self.select_products_stm.attach(self)

    def run(self):
        quit = False
        while not quit:
            choice = input('Doriti sa folositi Vending-ul? [d/n/quit] ')
            self.take_money_stm.current_state.client_arrived()

            match choice:
                case 'd':
                    moneyquit = False
                    while not moneyquit:
                        choice = input('Cat doriti sa inserati? [0.10/0.50/1/5/10/gata] ')
                        match choice:
                            case '0.10':
                                self.take_money_stm.insert_money_state.insert_10bani()
                            case '0.50':
                                self.take_money_stm.insert_money_state.insert_50bani()
                            case '1':
                                self.take_money_stm.insert_money_state.insert_1leu()
                            case '5':
                                self.take_money_stm.insert_money_state.insert_5lei()
                            case '10':
                                self.take_money_stm.insert_money_state.insert_10lei()
                            case 'gata':
                                moneyquit = True
                    self.select_products_stm.choose_another_product()
                case 'n':
                    pass
                case 'quit':
                    quit = True

    def proceed_to_checkout(self):
        if self.take_money_stm.money >= int(self.select_products_stm.current_state.price * 100):
            self.take_money_stm.add_money(-int(self.select_products_stm.current_state.price * 100))
            print(f'Ati primit o {self.select_products_stm.current_state.__class__.__name__}')
            choice = input('Doriti sa selectati un alt produs? [d/n] ')

            match choice.lower():
                case 'd':
                    self.select_products_stm.choose_another_product()
                case 'n':
                    print(f'Restul dvs. este {self.take_money_stm.money / 100}')
                    self.take_money_stm.update_amount_of_money(0)
                    self.take_money_stm.current_state = self.take_money_stm.wait_state

        else:
            print(f'Nu ati inserat destui bani, disponibili: {self.take_money_stm.money / 100}, necesari: {self.select_products_stm.current_state.price}')

    def update(self):
        self.proceed_to_checkout()


if __name__ == '__main__':
    vending_machine = VendingMachineSTM()
    vending_machine.run()
