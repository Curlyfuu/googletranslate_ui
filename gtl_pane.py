import threading
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QMouseEvent, QCloseEvent, QIcon
from PyQt5.QtWidgets import QWidget, QApplication
from resource.gtl import Ui_Form
from gtl_functions import *
from requests import get
import pyperclip
import time

status_flag = 1
url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}&ie=UTF-8&oe=UTF-8"
try:
    old_text = pyperclip.paste()
except:
    pass
translation = ""
# 生成词汇表和历史记录
doc_create()
# 从config_gtl.json中获取配置
config = load_config()

try:
    f_op = config["最低透明度"]
except:
    f_op = 0.6

try:
    f_opchange = config["渐变"]
except:
    f_opchange = True

try:
    f_soucela = config["源语言"]
except:
    f_soucela = 'en'

try:
    f_targetla = config["目标语言"]
except:
    f_targetla = 'zh-CN'


class Window(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.rs = 0
        self.desktop = QApplication.desktop()
        # 获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        self.pauseStatus = False
        # 从json文件中读取设置的高度和宽度，否则设置为屏幕的1/4大小
        try:
            self.f_width = config["宽度"]
        except:
            self.f_width = self.width / 2
        try:
            self.f_height = config["高度"]
        except:
            self.f_height = self.height / 2
        # 窗口状态：用于控制翻译线程的运行，多线程学得不好，应该会有更好的写法
        self.exit_state = 0
        if f_opchange == 1:
            self.setWindowOpacity(f_op)
        else:
            self.setWindowOpacity(1.0)
        # 始终将窗口置顶
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(0, 0)
        self.resize(self.f_width, self.f_height)

    # 响应"我看懂了"按键，只是隐藏，再次复制时会自动出现
    def exit_btn(self):
        if not self.pauseStatus:
            self.pushButton_2.setText('继续')
            self.pauseStatus = True
        else:
            self.pushButton_2.setText('暂停')
            self.pauseStatus = False

    def cp_source(self):
        pyperclip.copy(old_text)

    # 清除文本框
    def clear_text(self):
        self.output_text.clear()

    # 响应按键的退出
    def exit_all(self):
        self.exit_state = 1
        self.close()

    # 将窗口移动到左上方（top left，下面同理）
    def mv_tl(self):
        self.move(0, 0)

    def mv_tr(self):
        self.move(self.width - self.f_width, 0)

    def mv_bl(self):
        self.move(0, self.height - self.f_height)

    def mv_br(self):
        self.move(self.width - self.f_width, self.height - self.f_height)

    # 响应状态栏的右键退出
    def closeEvent(self, e: QCloseEvent):
        self.exit_state = 1
        self.close()

    # 重写移动事件，响应窗口的拖动
    def mouseMoveEvent(self, e: QMouseEvent):
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

    # 响应鼠标移入，并做渐变效果
    def enterEvent(self, event):
        op = f_op
        if f_opchange == 1:
            while op <= 1:
                self.setWindowOpacity(op)
                op += 0.05
                time.sleep(0.03)
            self.setWindowOpacity(1.0)

    # 响应鼠标移出，并做渐变效果
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


    # 后台翻译线程
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
                """
                判断上一次的输入结果和这一次的输入是否相等；
                上一次的输出与这一次的输入是否相等（由于程序将翻译结果又打印在了剪切板上【见下方代码】）
                这两步是必须的，不然会一直发请求，一直翻译同一段文本
                """
                if old_text != text and translation != text and not window.pauseStatus:
                    old_text = text
                    window.activateWindow()
                    translation = ""
                    # 消除复制文本中的回车和换行选项，对pdf复制的文本尤其适用
                    iput = text.replace('\r\n', ' ')
                    im = iput.replace('\n', ' ')
                    # 翻译 % 会产生乱码，替换为 percent，下同理
                    im = im.replace('%', ' percent')
                    im = im.replace('&', 'and')
                    full_url = url.format(f_soucela, f_targetla, im)
                    try:
                        r = get(full_url)
                        # 太过于频繁的复制，谷歌会返回429，需要等待一到两个小时（经验）后方可恢复
                        if r.status_code == 429:
                            window.output_text.append('\n*****频繁访问，需要等待大约一个小时*****\n')
                        else:
                            # 从返回的json中提取翻译结果
                            if r.json()[0] is not None:
                                for item in r.json()[0]:
                                    if item[0] is not None:
                                        try:
                                            translation += item[0].replace('\r', '')
                                        except:
                                            pass
                            # 将翻译结果打印到窗口中
                            window.output_text.append("　　" + translation)
                    except:
                        window.output_text.append('\n*****出错了，请检查网络连通性！*****\n')
                    try:
                        # 将打印结果写入剪切板中
                        pyperclip.copy(translation)
                    except:
                        window.output_text.append("****剪切板错误，请手动复制翻译结果！****\n")
                    try:
                        # 将结果写入到单词本和历史记录中
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
