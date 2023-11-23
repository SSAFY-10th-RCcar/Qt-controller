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
AUTH_PLUGIN = os.getenv("AUTH_PLUGIN")

SENSING_DELAY = 1000  # ms
SENSING_LOG_MAX = 15
QUERY_DELAY = 10  # ms

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.db = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_SCHEMA,
                                          auth_plugin=AUTH_PLUGIN)
        self.cur = self.db.cursor()
        self.ui.sensingText.clear()
        self.current_pressed = set()
        self.wasd = [0, 0, 0, 0]
        self.key_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.key_listener.start()

        self.query_que = list(set())

        self.ui.btn_w.setCheckable(True)
        self.ui.btn_a.setCheckable(True)
        self.ui.btn_s.setCheckable(True)
        self.ui.btn_d.setCheckable(True)

        self.ui.btn_forward.clicked.connect(self.forward)
        self.ui.btn_backward.clicked.connect(self.backward)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_leftforward.clicked.connect(self.leftforward)
        self.ui.btn_rightforward.clicked.connect(self.rightforward)
        self.ui.btn_leftbackward.clicked.connect(self.leftbackward)
        self.ui.btn_rightbackward.clicked.connect(self.rightbackward)

        # log
        self.log = []
        self.sensing = []

        # sensing data
        self.ui.sensingText.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(60, 60, 60);")
        self.sensingDataNum = 0
        self.ui.record_num.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(60, 60, 60);")
        self.ui.record_num.setText("records: 0")

        # sense timer setting
        self.senseTimer = QTimer()
        self.senseTimer.setInterval(SENSING_DELAY)
        self.senseTimer.timeout.connect(self.pollingQuery)
        self.senseTimer.start()

        # query timer setting
        self.queryTimer = QTimer()
        self.queryTimer.setInterval(QUERY_DELAY)
        self.queryTimer.timeout.connect(self.executeQuery)
        self.queryTimer.start()

    def on_press(self, key):
        new = self.wasd.copy()

        if key == pynput.keyboard.KeyCode.from_char('w'):
            new[0] = 1
            self.ui.btn_w.setChecked(True)
        if key == pynput.keyboard.KeyCode.from_char('a'):
            new[1] = 1
            self.ui.btn_a.setChecked(True)
        if key == pynput.keyboard.KeyCode.from_char('s'):
            new[2] = 1
            self.ui.btn_s.setChecked(True)
        if key == pynput.keyboard.KeyCode.from_char('d'):
            new[3] = 1
            self.ui.btn_d.setChecked(True)

        if new != self.wasd:
            self.wasd = new
            self.pushQuery()

    def on_release(self, key):
        if key == pynput.keyboard.KeyCode.from_char('w'):
            self.wasd[0] = 0
            self.ui.btn_w.setChecked(False)
        if key == pynput.keyboard.KeyCode.from_char('a'):
            self.wasd[1] = 0
            self.ui.btn_a.setChecked(False)
        if key == pynput.keyboard.KeyCode.from_char('s'):
            self.wasd[2] = 0
            self.ui.btn_s.setChecked(False)
        if key == pynput.keyboard.KeyCode.from_char('d'):
            self.wasd[3] = 0
            self.ui.btn_d.setChecked(False)
        self.pushQuery()

    def pushQuery(self):
        query = "update wasd set w = %s, a = %s, s = %s, d = %s, is_finish = 0 where id = 1"
        value = (self.wasd[0], self.wasd[1], self.wasd[2], self.wasd[3])
        self.query_que.append(((query, value)))

    def executeQuery(self):
        # execute one query
        if len(self.query_que) > 0:
            query, value = self.query_que.pop(0)
            self.cur.execute(query, value)
            self.db.commit()
            # print("Executed query: " + query + " with value: " + str(value))

    def pollingQuery(self):
        self.cur.execute("select time, pressure, temp, humid, velo from sensing where id = 1")
        for (time, pressure, temp, humid, velo) in self.cur:
            str = "%s:  기압: %4s  |  온도: %4s  |  습도: %4s  |  속도: %4s" % (
            time.strftime("%Y-%m-%d %H:%M:%S"), pressure, temp, humid, velo)
            self.sensing.insert(0, str)
            if len(self.sensing) > SENSING_LOG_MAX:
                self.sensing.pop()
                self.sensingDataNum -= 1
            self.ui.sensingText.setText('\n'.join(self.sensing))
        self.sensingDataNum += 1
        if self.sensingDataNum >= SENSING_LOG_MAX:
            str = "records: 15(max)"
        else:
            str = "records: %d" % self.sensingDataNum
        self.ui.record_num.setText(str)
        self.db.commit()

    def closeEvent(self, event):
        self.cur.close()
        self.db.close()

    def forward(self):
        self.wasd = [1, 0, 0, 0]
        self.pushQuery()

    def stop(self):
        self.wasd = [0, 0, 0, 0]
        self.pushQuery()

    def backward(self):
        self.wasd = [0, 0, 1, 0]
        self.pushQuery()

    def leftforward(self):
        self.wasd = [1, 1, 0, 0]
        self.pushQuery()

    def rightforward(self):
        self.wasd = [1, 0, 0, 1]
        self.pushQuery()

    def leftbackward(self):
        self.wasd = [0, 1, 1, 0]
        self.pushQuery()

    def rightbackward(self):
        self.wasd = [0, 0, 1, 1]
        self.pushQuery()

app = QApplication()
win = MyApp()
win.show()
app.exec()
