from abc import ABC, abstractmethod
from commands import *


class Handler(ABC):
    command: Command

    def __init__(self, command: Command):
        self.command = command

    @abstractmethod
    def handle(self, file: str):
        pass


class BashHandler(Handler):
    next: Handler | None

    def __init__(self, next: Handler | None):
        super().__init__(BashCommand())
        self.next = next

    def handle(self, file: str):
        if self.looks_like_bash(file):
            pass  # TODO
        elif self.next is not None:
            self.next.handle(file)

    @staticmethod
    def looks_like_bash(file: str) -> bool:
        if file.startswith("#!/usr/bin/bash") or file.startswith("#!/usr/bin/env bash") or file.startswith("/bin/bash"):
            return True
        return False


class PythonHandler(Handler):
    next: Handler | None

    def __init__(self, next: Handler | None):
        self.next = next

    def handle(self, file: str):
        if self.looks_like_python(file):
            pass  # TODO
        elif self.next is not None:
            self.next.handle(file)

    @staticmethod
    def looks_like_python(file: str) -> bool:
        if file.startswith("#!/usr/bin/python"):
            return True

        if "@staticmethod" in file and "from" in file:
            return True

        return False


class KotlinHandler(Handler):
    next: Handler | None

    def __init__(self, next: Handler | None):
        self.next = next

    def handle(self, file: str):
        if self.looks_like_kotlin(file):
            pass  # TODO
        elif self.next is not None:
            self.next.handle(file)

    @staticmethod
    def looks_like_kotlin(file: str) -> bool:
        return ";" not in file


class JavaHandler(Handler):
    next: Handler | None

    def __init__(self, next: Handler | None):
        self.next = next

    def handle(self, file: str):
        if self.looks_like_java(file):
            pass  # TODO
        elif self.next is not None:
            self.next.handle(file)

    @staticmethod
    def looks_like_java(file: str) -> bool:
        return ";" in file

