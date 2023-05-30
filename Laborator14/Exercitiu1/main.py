from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.consult('Exercitiul1.pl')

    print('======= SUBPUNCTUL 1 =======')
    print('e pereche de membri au o mătusă?')
    for soln in prolog.query('matusa(X, Y)'):
        print(f'{soln["Y"]} este matusa a lui {soln["X"]}')
    print('\n')

    print('======= SUBPUNCTUL 2 =======')
    print('e pereche de membri au un bunic?')
    for soln in prolog.query('bunicul(X, Y)'):
        print(f'{soln["Y"]} este bunicul lui {soln["X"]}')
    print('\n')

    print('======= SUBPUNCTUL 3 =======')
    print('Cine este sora lui George?')
    for soln in prolog.query('sora(george, Y)'):
        print(f'{soln["Y"]} este o sora a lui george')
