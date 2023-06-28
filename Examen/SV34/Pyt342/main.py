import tkinter as tk


WIDTH = 640
HEIGHT = 480


def series(n):
    return n + (n-4) * (n-3) / 2


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Function graph')
    root.geometry(f'{WIDTH}x{HEIGHT+40}')

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack(anchor='center', expand=True)

    label_text = tk.StringVar(value='No point selected')
    label = tk.Label(root, textvariable=label_text)
    label.pack(anchor='s', expand=True)

    print(f'end={series(50)}, start={series(20)}')
    for i in range(20, 50, 1):
        si = series(i)
        x, y = i, si / 2
        radius = 4
        point_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red')
        canvas.tag_bind(point_id, '<Button-1>', lambda _, i=i, si=si: label_text.set(f'i={i}, si={si}'))

    root.mainloop()
