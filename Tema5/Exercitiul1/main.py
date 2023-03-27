from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir


def on_browse_button_clicked(button, input_box):
    file = QFileDialog.getOpenFileName(button, "Open File", QDir.currentPath())
    print(file)
    input_box.setText(file[0])


def main():
    app = QApplication([])
    app.setApplicationName('Tema5/Exercitiul 1')

    widget = QWidget()
    grid = QGridLayout(widget)

    input_box = QLineEdit()
    input_box.setPlaceholderText("/path/to/file")
    input_box.setMinimumWidth(500)
    grid.addWidget(input_box, 0, 0)

    browse_button = QPushButton("browse")
    browse_button.clicked.connect(lambda: on_browse_button_clicked(browse_button, input_box))
    grid.addWidget(browse_button, 0, 1)

    result_view = QTextEdit()
    result_view.setPlaceholderText("Result")
    grid.addWidget(result_view, 1, 0)

    button_container = QWidget()
    vertical_layout = QVBoxLayout(button_container)
    convert_to_html_button = QPushButton("Convert to HTML")
    send_button = QPushButton("Send to C program")
    vertical_layout.addWidget(convert_to_html_button)
    vertical_layout.addWidget(send_button)
    grid.addWidget(button_container, 1, 1)

    widget.show()

    app.exec_()


if __name__ == '__main__':
    main()
