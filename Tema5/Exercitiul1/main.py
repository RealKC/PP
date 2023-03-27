from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
import sysv_ipc


def on_browse_button_clicked(button, input_box):
    file = QFileDialog.getOpenFileName(button, 'Open File', QDir.currentPath(), filter="Text Files (*.txt)")
    print(file)
    if len(file[0]) > 0:
        input_box.setText(file[0])


def convert_file_to_html(file):
    with open(file, 'r') as file:
        contents = file.read()
    result = ""

    first = True
    for line in contents.splitlines():
        if len(line) == 0:
            continue

        if first:  # prima linie e titlul
            result += f"<h1>{line}</h1>"
            first = False
        else:
            result += f"<p>{line}</p>"

    return result


def on_convert_to_html_clicked(file, result_box):
    html = convert_file_to_html(file)
    result_box.setText(html)


def on_send_clicked(file_name, html):
    mq = sysv_ipc.MessageQueue(-1)
    mq.send(file_name, type=1)
    mq.send(html, type=2)


def main():
    app = QApplication([])
    app.setApplicationName('Tema5/Exercitiul 1')

    widget = QWidget()
    grid = QGridLayout(widget)

    input_box = QLineEdit()
    input_box.setPlaceholderText("/path/to/file")
    input_box.setMinimumWidth(500)
    grid.addWidget(input_box, 0, 0)

    browse_button = QPushButton('Browse')
    browse_button.clicked.connect(lambda: on_browse_button_clicked(browse_button, input_box))
    grid.addWidget(browse_button, 0, 1)

    result_view = QTextEdit()
    result_view.setPlaceholderText('Result')
    result_view.setReadOnly(True)
    grid.addWidget(result_view, 1, 0)

    button_container = QWidget()
    vertical_layout = QVBoxLayout(button_container)

    convert_to_html_button = QPushButton('Convert to HTML')
    convert_to_html_button.clicked.connect(lambda: on_convert_to_html_clicked(input_box.text(), result_view))

    send_button = QPushButton('Send to C program')
    send_button.clicked.connect(lambda: on_send_clicked(input_box.text(), result_view.toHtml()))

    vertical_layout.addWidget(convert_to_html_button)
    vertical_layout.addWidget(send_button)
    grid.addWidget(button_container, 1, 1)

    widget.show()

    app.exec_()


if __name__ == '__main__':
    main()
