import multiprocessing
from abc import abstractmethod, ABC
from multiprocessing.connection import Listener, Client
from random import randint
from time import sleep


class ProcessWithSocket(multiprocessing.Process, ABC):
    def __init__(self, /, rx_addr, tx_addr):
        super().__init__()
        self.listener = Listener(rx_addr) if rx_addr is not None else None
        self.tx = tx_addr

    def send(self, msg):
        self.client = Client(self.tx)
        self.client.send(msg)

    @abstractmethod
    def run(self):
        pass


class MultiplicationProcess(ProcessWithSocket):
    def __init__(self, lst: list[int], alpha: int, tx_addr):
        super().__init__(None, tx_addr)
        self.lst = lst
        self.alpha = alpha

    def run(self):
        print(f'[{self.name}] Started multiplying')
        lst = []
        for i in range(len(self.lst)):
            lst.append(self.lst[i] * self.alpha)
        self.send(lst)
        print(f'[{self.name}] Done multiplying')


class SortingProcess(ProcessWithSocket):
    def __init__(self, rx_addr, tx_addr):
        super().__init__(rx_addr, tx_addr)

    def run(self):
        print(f'[{self.name}] Started sorting')
        conn = self.listener.accept()
        lst = conn.recv()
        lst.sort()
        self.send(lst)
        print(f'[{self.name}] Done sorting')


class PrintingProcess(ProcessWithSocket):
    def __init__(self, rx_addr):
        super().__init__(rx_addr, None)

    def run(self):
        conn = self.listener.accept()
        msg = conn.recv()
        print(f'[{self.name}] Received: {msg}')


if __name__ == '__main__':
    multiplication = 'localhost', 3000
    sorting = 'localhost', 3001

    jobs = [MultiplicationProcess(
        lst=[randint(0, 100000) for i in range(100)],
        alpha=randint(0, 10),
        tx_addr=multiplication
    ), SortingProcess(rx_addr=multiplication, tx_addr=sorting), PrintingProcess(rx_addr=sorting)]

    for job in jobs:
        job.start()

    for job in jobs:
        job.join()