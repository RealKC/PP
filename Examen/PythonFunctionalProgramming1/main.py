from functools import reduce
from pprint import pprint

from more_itertools import map_reduce
from functional import seq

def read_file(file) -> str:
    with open(file, 'r') as f:
        return f.read()


if __name__ == '__main__':
    documente = ['document1.txt', 'document2.txt']

    continut = map(lambda doc: (doc, read_file(doc).split()), documente)  # [(a, [b, c, d]), (e, [f, g, h])]
    cuvinte = reduce(lambda x, y: x + y,  # [(a, b), (a, c), (a, d), (e, f), (e, g), (e, h)]
                     map(lambda cont: list(map(lambda w: (cont[0], w), cont[1])), continut))  # [[(a, b), (a, c), (a, d)], [(e, f), (e, g), (e, )]]

    texte_intermediare = dict(map_reduce(
        cuvinte,  # cuvintele sunt perechi (document, cuvant)
        keyfunc=lambda document_si_word: document_si_word[1],
        valuefunc=lambda document_si_word: (document_si_word[0], 1),
        # [("doc1", 1), ("doc2", 1), ("doc1", 1), ("doc1", 1)]
        reducefunc=lambda s: seq(s).reduce_by_key(lambda x, y: x + y)
    ))

    pprint(texte_intermediare)

