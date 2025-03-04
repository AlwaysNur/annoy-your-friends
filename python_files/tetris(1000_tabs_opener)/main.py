import sys
import threading
import time
import webbrowser
from PyQt5.QtWidgets import QWidget, QApplication

def open_wins(wait_time):
    time.sleep(wait_time)
    for i in range(1000):
        webbrowser.open("https://google.com")

t1 = threading.Thread(target=open_wins, args=(2,))

class Widget(QWidget):
    def __init__(self):
        super().__init__()


    def closeEvent(self, a0):
        print("bye")
        a0.ignore()


app = QApplication(sys.argv)
window = Widget()
window.show()
t1.start()
sys.exit(app.exec())



