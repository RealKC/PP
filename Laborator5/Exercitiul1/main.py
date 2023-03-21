import os
import tkinter as tk


def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False

    for d in range(3, int(n / 2), 2):
        if n % d == 0:
            return False

    return True


class Parser:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    A = None
    B = None

    def __init__(self, gui):
        self.result = "Result"
        self.integer_list = []

        self.gui = gui
        self.gui.title('Exemplul 1 cu Tkinter')

        self.gui.geometry("600x300")

        self.integer_list_lbl = tk.Label(master=self.gui,
                                         text="List of integers:")

        self.add_list_btn = tk.Button(master=self.gui,
                                      text="Add list",
                                      command=self.add_list)

        self.filter_primes_btn = tk.Button(master=self.gui, text="Filter primes", command=self.filter_primes)
        self.filter_odd_btn = tk.Button(master=self.gui, text="Filter odd", command=self.filter_odd)
        self.sum_numbers_btn = tk.Button(master=self.gui, text="Sum numbers", command=self.sum_numbers)

        self.integer_list_text = tk.Text(self.gui, width=50, height=1)
        self.integer_list_text.insert(tk.END, str(list(range(1, 16)))[1:-1])

        self.result_text_box = tk.Text(self.gui, width=50, height=10)
        self.result_text_box.insert(tk.END, self.result)

        # alignment on the grid
        self.integer_list_lbl.grid(row=0, column=0)
        self.result_text_box.grid(row=1, column=1)
        self.integer_list_text.grid(row=0, column=1)
        self.add_list_btn.grid(row=0, column=2)
        self.filter_primes_btn.grid(row=1, column=2)
        self.filter_odd_btn.grid(row=2, column=2)
        self.sum_numbers_btn.grid(row=3, column=2)

        self.gui.mainloop()

    def update_result(self, result):
        self.result = str(result)
        self.result_text_box.insert(tk.END, f"\n{self.result}")

    def add_list(self):
        result = self.integer_list_text.get("1.0", tk.END)
        result = result.strip().replace(' ', '')
        result = [int(item) for item in result.split(',')]
        self.integer_list = result
        self.update_result(self.integer_list)
        print(result)

    def filter_primes(self):
        new_list = []
        for i in range(len(self.integer_list)):
            if is_prime(int(self.integer_list[i])):
                new_list.append(self.integer_list[i])
        self.integer_list = new_list
        self.update_result(self.integer_list)

    def filter_odd(self):
        self.integer_list = list(filter(lambda n: int(n) % 2 == 0, self.integer_list))
        self.update_result(self.integer_list)

    def sum_numbers(self):
        thesum = sum(self.integer_list)
        self.update_result(thesum)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Exemplul 1 cu Tkinter')
    app = Parser(root)
    root.mainloop()
