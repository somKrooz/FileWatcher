import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton , QLabel
from PyQt5.QtCore import Qt  , QProcess
from PyQt5 import QtGui
import tempfile


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon('Data/Cool.png'))
        self.setWindowTitle('observer')
        self.setGeometry(150, 150, 300, 200)

        self.text_field = QLineEdit(self)
        self.text_field.setPlaceholderText("Enter Path")

        self.message_field = QLabel(self)
        self.message_field.setText("...")
        self.message_field.setAlignment(Qt.AlignCenter)
        self.message_field.setStyleSheet("QLineEdit { padding: 5px; }")


        self.print_button = QPushButton('Change Path', self)
        self.print_button.clicked.connect(self.print_text)

        layout = QVBoxLayout()
        layout.addWidget(self.text_field)
        layout.addWidget(self.message_field)
        layout.addWidget(self.print_button)
        self.setLayout(layout)

    def print_text(self):
        text = self.text_field.text()
        temp_folder_path = tempfile.gettempdir()
        temp = f'{(temp_folder_path)}\\WatcherCache.txt' 
        with open(temp, 'w') as file:
            file.write(str(text))
        with open(temp, "r") as f:
            for line in f:
                self.message_field.setText(f"Watching: {line.strip()}")
            
    def showEvent(self, event):
        self.process = QProcess(self)
        self.process.start("C:\\Users\\somkr\\source\\repos\\Trying\\x64\\Debug\\Trying.exe")

        temp_folder_path = tempfile.gettempdir()
        temp = f'{(temp_folder_path)}\\WatcherCache.txt' 
        with open(temp, "r") as f:
            for line in f:
                self.message_field.setText(f"Watching: {line.strip()}")

         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    