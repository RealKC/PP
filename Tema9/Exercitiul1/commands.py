import subprocess
from subprocess import PIPE
from abc import ABC, abstractmethod
from tempfile import NamedTemporaryFile


class Command(ABC):
    @abstractmethod
    def execute(self, program: str):
        pass


class BashCommand(Command):
    def execute(self, program: str):
        proc = subprocess.run(["/usr/bin/bash", "-c", program], stdout=PIPE, stderr=PIPE)

        print(f"return code = {proc.returncode}")
        print(f"stdout = {proc.stdout}")
        print(f"stderr = {proc.stderr}")


class PythonCommand(Command):
    def execute(self, program: str):
        proc = subprocess.run(["/usr/bin/python", "-c", program], stdout=PIPE, stderr=PIPE)

        print(f"return code = {proc.returncode}")
        print(f"stdout = {proc.stdout}")
        print(f"stderr = {proc.stderr}")


class KotlinCommand(Command):
    def execute(self, program: str):
        with NamedTemporaryFile(mode="w+", suffix=".kt") as fp:
            fp.write(program)
            fp.flush()
            output_name = '/tmp/kotlin-temp.jar'

            proc = subprocess.run(["/usr/bin/kotlinc-jvm", fp.name, "-include-runtime", '-d', output_name])

            print(f"[kotlinc] return code = {proc.returncode}")
            print(f"[kotlinc] stdout = {proc.stdout}")
            print(f"[kotlinc] stderr = {proc.stderr}")

            if proc.returncode != 0:
                print('Failed to execute kotlin compiler, leaving...')

            proc = subprocess.run(["java", "-jar", output_name], stdout=PIPE, stderr=PIPE)

            print(f"[program] return code = {proc.returncode}")
            print(f"[program] stdout = {proc.stdout}")
            print(f"[program] stderr = {proc.stderr}")


class JavaCommand(Command):
    def execute(self, program: str):
        start = 0
        for idx, ch in enumerate(program):
            if ch.isupper():
                start = idx
                break
        end = program.find("{") - 1
        classname = program[start:end]

        with open(f"/tmp/{classname}.java", mode="w") as fp:
            fp.write(program)
            fp.flush()
            proc = subprocess.run(["java", fp.name], stdout=PIPE, stderr=PIPE)

            print(f"[program] return code = {proc.returncode}")
            print(f"[program] stdout = {proc.stdout}")
            print(f"[program] stderr = {proc.stderr}")
