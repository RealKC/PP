import datetime
import time
import tkinter as tk

from PIL import ImageGrab


class MouseEventProcessor:
    root: tk.Tk
    canvas: tk.Canvas

    line_start: tuple[int, int]
    line_end: tuple[int, int]

    line_id = None

    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root

    def push_event(self, event: tk.Event):
        if event.type == tk.EventType.Motion:
            self.mouse_moved(event.x, event.y)
        elif event.type == tk.EventType.ButtonPress:
            self.started_drawing(event.x, event.y)
        elif event.type == tk.EventType.ButtonRelease:
            self.finished_drawing()

        self.root.title(f'line from ({self.line_start[0]}, {self.line_start[1]}) -> ({self.line_end[0]}, {self.line_end[1]})')

    def mouse_moved(self, x, y):
        if self.line_id is not None:
            canvas.delete(self.line_id)
        self.line_end = x, y
        self.line_id = canvas.create_line(self.line_start, self.line_end, width=4, fill='red')

    def started_drawing(self, x, y):
        self.line_start = self.line_end = x, y

    def finished_drawing(self):
        self.line_id = None


def save(widget, root, file_menu):
    file_menu.pack_forget()
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(f'{datetime.datetime.now()}.png')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('640x480')  # God's Holy Resolution

    canvas = tk.Canvas(root, width=640, height=440, bg='white')
    canvas.pack(anchor=tk.CENTER, expand=True)

    event_processor = MouseEventProcessor(canvas, root)

    canvas.bind('<ButtonPress-1>', lambda event: event_processor.push_event(event))
    canvas.bind('<ButtonRelease-1>', lambda event: event_processor.push_event(event))
    canvas.bind('<B1-Motion>', lambda event: event_processor.push_event(event))

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar)
    file_menu.add_command(label='Save', command=lambda: save(canvas, root, file_menu))
    file_menu.add_command(label='Exit', command=root.destroy)
    menubar.add_cascade(label='File', menu=file_menu, underline=0)

    root.mainloop()
