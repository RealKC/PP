class Memento:
    def __init__(self, past_idx, past_list):
        self.idx = past_idx
        self.list = past_list

class Processer:
    def __init__(self, input):
        self.date = input
        self.curr_idx = 0
        self.memento_stack = []

    def restore_from(self, memento: Memento):
        self.curr_idx = memento.idx
        self.date = memento.list

    def save_to_memento(self) -> Memento:
        return Memento(self.curr_idx, self.date)

    def apply_function(self, func):
        self.memento_stack.append(self.save_to_memento())
        self.date[self.curr_idx] = func(self.date[self.curr_idx], self.curr_idx)
        self.curr_idx += 1

    def process(self):
        f1 = lambda x: x + 1 if x % 2 == 0 else x
        f2 = lambda x: 3*x*x - 2*x + 1
        f3 = lambda i: self.date[i] + self.date[i + 1]

        idx = self.curr_idx
        choice = input(f'[idx={idx}, val={self.date[idx]}] Apply f1, f2, f3 or go back? [1,2,3,b]: ')

        match choice:
            case '1':
                self.apply_function(lambda x, _: f1(x))
            case '2':
                self.apply_function(lambda x, _: f2(x))
            case '3':
                self.apply_function(lambda _, i: f3(i))
            case 'b':
                memento = self.memento_stack.pop()
                self.restore_from(memento)

    def done(self) -> bool:
        return self.curr_idx == len(self.date)


def read_date() -> list[int]:
    with open('input.txt', 'r') as f:
        return list(map(lambda s: int(s), f.read().split()))


if __name__ == '__main__':
    proc = Processer(read_date())

    while not proc.done():
        proc.process()

    print(f'At the end we got: {proc.date}')
