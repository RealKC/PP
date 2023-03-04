import polyglot


def read_numbers():
    n = int(input("Introduceti numarul de aruncari: "))
    x = int(input("Introduceti x cu conditia 1 <= x <= n: "))
    while not(1 <= x <= n):
        x = int(input("Introduceti x cu conditia 1 <= x <= n: "))
    return n, x


def compute_probability(n, x):
    return polyglot.eval(language="R", string="""
prob <- function(n, x) {
    return(dbinom(x, n, 0.5))
}
""")(n, x)


def main():
    n, x = read_numbers()
    print(f'Probabilitate de a obtine de {x} ori pajura din {n} aruncari este {compute_probability(n, x)}')


if __name__ == "__main__":
    main()
