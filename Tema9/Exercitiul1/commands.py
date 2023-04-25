import subprocess
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, program: str):
        pass


class BashCommand(Command):
    def execute(self, program: str):
        proc = subprocess.run(["/usr/bin/bash", program])

        print(f"return code = {proc.returncode}")
        print(f"stdout = {proc.stdout}")
        print(f"stderr = {proc.stderr}")


class PythonCommand(Command):
    def execute(self, program: str):
        proc = subprocess.run(["/usr/bin/python", program])

        print(f"return code = {proc.returncode}")
        print(f"stdout = {proc.stdout}")
        print(f"stderr = {proc.stderr}")


class KotlinCommand(Command):
    def execute(self, program: str):
        pass


class JavaCommand(Command):
    def execute(self, program: str):
        pass
