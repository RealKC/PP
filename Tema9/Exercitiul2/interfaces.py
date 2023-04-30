from abc import ABC
import inspect


class State(ABC):
    pass


class Observable:
    observers: list[object]

    def __init__(self):
        self.observers = []

    def attach(self, obj):
        self.observers.append(obj)

    def dettach(self, obj):
        self.observers.remove(obj)

    def notify_all(self, argument=None):
        for observer in self.observers:
            sig = inspect.signature(observer.update)
            positional_argument_count = sum(1 for param in sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD)
            match positional_argument_count:
                case 0:
                    observer.update()
                case 1:
                    observer.update(argument)
