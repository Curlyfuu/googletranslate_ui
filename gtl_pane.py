import threading
from PyQt5.Qt import *
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication
from resource.gtl import Ui_Form
from gtl_functions import *
import requests
import pyperclip
import time

status_flag = 1
url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}&ie=UTF-8&oe=UTF-8"
old_text = ""
translation = ""
doc_create()
config = load_config()
f_width = config["宽度"]
f_height = config["高度"]
f_op = config["最低透明度"]
f_opchange = config["渐变"]


class Window(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.exit_state = 0
        if f_opchange == 1:
            self.setWindowOpacity(f_op)
        else:
            self.setWindowOpacity(1.0)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.move(100, 100)
        self.resize(f_width, f_height)

    def exit_btn(self):
        self.hide()

    def cp_source(self):
        pyperclip.copy(old_text)

    def clear_text(self):
        self.output_text.clear()

    def exit_all(self):
        self.exit_state = 1
        self.close()

    def closeEvent(self, e: QCloseEvent):
        self.exit_state = 1
        self.close()


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        # LeftButton = 1
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        # LeftButton = 1
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def enterEvent(self, event):
        op = f_op
        if f_opchange == 1:
            while op <= 1:
                self.setWindowOpacity(op)
                op += 0.05
                time.sleep(0.03)
            self.setWindowOpacity(1.0)

    def leaveEvent(self, event):
        op = 1.0
        if f_opchange == 1:
            while op >= f_op:
                self.setWindowOpacity(op)
                op -= 0.05
                time.sleep(0.03)
            self.setWindowOpacity(f_op)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('gtl.ico'))
    window = Window()

    def fun01():
        global translation, old_text, status_flag
        while True:
            if window.exit_state == 1:
                app.exit(0)
                exit(0)
            try:
                text = pyperclip.paste()
                text = text.replace('\r\n', ' ')
                pyperclip.copy(text)
                if old_text != text and translation != text:
                    window.show()
                    translation = ""
                    iput = text.replace('\r\n', ' ')
                    im = iput.replace('\n', ' ')
                    im = im.replace('%', ' percent')
                    im = im.replace('&', 'and')
                    old_text = text
                    full_url = url.format('en', "zh-CN", im)
                    try:
                        r = requests.get(full_url)
                        if r.status_code == 429:
                            window.output_text.append('\n*****频繁访问，需要等待大约一个小时*****\n')
                        else:
                            if r.json()[0] != None:
                                for item in r.json()[0]:
                                    if item[0] != None:
                                        try:
                                            translation += item[0].replace('\r', '')
                                        except:
                                            pass
                            window.output_text.append("　　" + translation)
                    except:
                        window.output_text.append('\n*****出错了，请检查网络连通性！*****\n')
                    try:
                        pyperclip.copy(translation)
                    except:
                        window.output_text.append("****剪切板错误，请手动复制翻译结果！****\n")
                    try:
                        write_doc(im, translation)
                    except:
                        window.output_text.append("写入文件错误")
            except:
                pass
            time.sleep(0.2)

    t01 = threading.Thread(target=fun01)
    t01.start()
    window.show()
    sys.exit(app.exec_())
    t01.join()
