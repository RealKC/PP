import sys

from handlers import *

if __name__ == '__main__':
    print("Give me a script:")
    contents = sys.stdin.read()

    chain = BashHandler(PythonHandler(JavaHandler(KotlinHandler(None))))
    chain.handle(contents)
