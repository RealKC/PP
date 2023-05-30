from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.consult('Exercitiu2.pl')

    question = 'poatelua(stare(lausa, pepodea, lafereastra, nuarebanana))'
    answer = next(prolog.query(question))

    print(answer)
