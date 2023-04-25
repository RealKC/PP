from handlers import *

if __name__ == '__main__':
    contents = input("Give me a script:\n")

    chain = BashHandler(PythonHandler(JavaHandler(KotlinHandler(None))))
    chain.handle(contents)
