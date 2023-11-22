from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainUI import Ui_MainWindow
from pynput import keyboard
from dotenv import load_dotenv
import pynput.keyboard
import mysql.connector
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")
AUTH_PLUGIN= os.getenv("AUTH_PLUGIN")
DELAY = 100 #ms


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.db = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_SCHEMA, auth_plugin=AUTH_PLUGIN)
        self.cur = self.db.cursor()
        self.ui.sensingText.clear()
        self.ui.logText.clear()
        self.current_pressed = set()
        self.wasd = [0,0,0,0]
        self.key_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.key_listener.start()

        self.ui.btn_w.setStyleSheet("background-color: gray")
        self.ui.btn_a.setStyleSheet("background-color: gray")
        self.ui.btn_s.setStyleSheet("background-color: gray")
        self.ui.btn_d.setStyleSheet("background-color: gray")

        self.query_que = []

        #log
        self.log = []
        self.sensing = []

        #timer setting
        self.timer = QTimer()
        self.timer.setInterval(DELAY) #500ms
        self.timer.timeout.connect(self.executeQuery)
        self.timer.start()


    def on_press(self, key):
        new = self.wasd.copy()

        if key == pynput.keyboard.KeyCode.from_char('w'):
            new[0] = 1
            self.ui.btn_w.setStyleSheet("background-color: green")
        if key == pynput.keyboard.KeyCode.from_char('a'):
            new[1] = 1
            self.ui.btn_a.setStyleSheet("background-color: green")
        if key == pynput.keyboard.KeyCode.from_char('s'):
            new[2] = 1
            self.ui.btn_s.setStyleSheet("background-color: green")
        if key == pynput.keyboard.KeyCode.from_char('d'):
            new[3] = 1
            self.ui.btn_d.setStyleSheet("background-color: green")

        if new != self.wasd:
            self.wasd = new
            self.pushQuery()

    def on_release(self, key):
        if key == pynput.keyboard.KeyCode.from_char('w'):
            self.wasd[0] = 0
            self.ui.btn_w.setStyleSheet("background-color: gray")
        if key == pynput.keyboard.KeyCode.from_char('a'):
            self.wasd[1] = 0
            self.ui.btn_a.setStyleSheet("background-color: gray")
        if key == pynput.keyboard.KeyCode.from_char('s'):
            self.wasd[2] = 0
            self.ui.btn_s.setStyleSheet("background-color: gray")
        if key == pynput.keyboard.KeyCode.from_char('d'):
            self.wasd[3] = 0
            self.ui.btn_d.setStyleSheet("background-color: gray")

        self.pushQuery()

    def pushQuery(self):
        query = "update wasd set w = %s, a = %s, s = %s, d = %s where id = 1"
        value = (self.wasd[0], self.wasd[1], self.wasd[2], self.wasd[3])
        self.query_que.append((query, value))

    def executeQuery(self):
        # execute one query
        if len(self.query_que) > 0:
            query, value = self.query_que.pop(0)
            self.cur.execute(query, value)
            self.db.commit()


    def start(self):
        self.timer.start()


    def pollingQuery(self):
        self.cur.execute("select * from command order by time desc limit 7")
        self.ui.logText.clear()
        self.log.clear()
        self.sensing.clear()

        for (id, time, cmd_string, arg_string, is_finish) in self.cur:
            str = "%5d | %s | %6s | %6s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), cmd_string, arg_string, is_finish)
            self.log.append(str)
            self.ui.logText.setText('\n'.join(self.log))

        self.cur.execute("select * from sensing order by time desc limit 7")
        self.ui.sensingText.clear()
        for (id, time, num1, num2, num3, meta_string, is_finish) in self.cur:
            str = "%d | %s | %6s | %6s | %6s | %15s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), num1, num2, num3, meta_string, is_finish)
            self.sensing.append(str)
            self.ui.sensingText.setText('\n'.join(self.sensing))
        self.db.commit()

    def closeEvent(self, event):
        self.cur.close()
        self.db.close()

    def insertCommand(self, cmd_string, arg_string):
        time = QDateTime().currentDateTime().toPython()
        is_finish = 0

        query = "insert into command(time, cmd_string, arg_string, is_finish) values (%s, %s, %s, %s)"
        value = (time, cmd_string, arg_string, is_finish)

        self.cur.execute(query, value)
        self.db.commit()

    def insertWASD(self, w, a, s, d):
        time = QDateTime().currentDateTime().toPython()
        is_finish = 0

        query = "insert into wasd(w, a, s, d, time, is_finish) values (%s, %s, %s, %s, %s, %s)"
        value = (w, a, s, d, time, is_finish)

        self.cur.execute(query, value)
        self.db.commit()


    def go(self):
        self.insertCommand("go", "0")

    def stop(self):
        self.insertCommand("stop", "0")

    def back(self):
        self.insertCommand("back", "0")

    def left(self):
        self.insertCommand("left", "0")

    def mid(self):
        self.insertCommand("mid", "0")

    def right(self):
        self.insertCommand("right", "0")


app = QApplication()
win = MyApp()
win.show()
app.exec()
