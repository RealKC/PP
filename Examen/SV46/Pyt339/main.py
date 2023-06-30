import random
from abc import ABC, abstractmethod


class LogMessageHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, msg):
        raise NotImplementedError(f'ErrorHandlingStrategy: `handle` not implemented by {self.__class__.__name__}')


class WarningHandlingStrategy(LogMessageHandlingStrategy):
    def handle(self, msg):
        with open('warnings.txt', 'a') as f:
            f.write(f'{msg}\n')


class ErrorHandlingStrategy(LogMessageHandlingStrategy):
    def handle(self, msg):
        print(str(msg))
        with open('errors.txt', 'a') as f:
            f.write(f'{msg}\n')


class CriticalErrorHandlingStrategy(LogMessageHandlingStrategy):
    def handle(self, msg):
        with open('critical_errors.txt', 'a') as f:
            f.write(f'{msg}\n')
        exit(1)


class YoureBadException(Exception):
    def __str__(self):
        return 'You\'re bad'


class KindaBadException(Exception):
    def __str__(self):
        return 'Bruh'

def strategy_demonstration(strategy):
    exceptions = [YoureBadException, KindaBadException]

    try:
        raise random.choice(exceptions)()
    except Exception as e:
        strategy.handle(e)


if __name__ == '__main__':
    strategies = [WarningHandlingStrategy, ErrorHandlingStrategy, CriticalErrorHandlingStrategy]
    for _ in range(10):
        strategy_demonstration(random.choice(strategies)())
