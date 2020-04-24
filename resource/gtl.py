# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gtl.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(10000, 16777215))
        Form.setStyleSheet("QWidget#Form {\n"
"border-top-left-radius：10px; \n"
"border-top-right-radius：10px;\n"
"border-image: url(:/gtl_base/images/gtl_bg.jpg);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output_text = QtWidgets.QTextEdit(self.widget)
        self.output_text.setStyleSheet("border-radius: 10px;\n"
"font: 18pt \"华文楷体\";\n"
"background: transparent;")
        self.output_text.setObjectName("output_text")
        self.verticalLayout_2.addWidget(self.output_text)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background: transparent;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(60, 60))
        self.widget_3.setMaximumSize(QtCore.QSize(60, 60))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    margin: 0;\n"
"    border-image: url(:/gtl_base/images/tl.png);\n"
"    padding: 0;\n"
"    border: none;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    margin: 0;\n"
"    border-image: url(:/gtl_base/images/tl.png);\n"
"    padding: 0;\n"
"    border: none;\n"
"\n"
"    border-radius: 4px;\n"
"    background-color: rgb(250, 224, 129);\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    margin: 0;\n"
"    border-image: url(:/gtl_base/images/tr.png);\n"
"padding: 0;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"margin: 0;\n"
"border-image: url(:/gtl_base/images/tr.png);\n"
"padding: 0;\n"
"border: none;\n"
"\n"
"background-color: rgb(250, 224, 129);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"margin: 0;\n"
"border-image: url(:/gtl_base/images/bl.png);\n"
"padding: 0;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"margin: 0;\n"
"border-image: url(:/gtl_base/images/bl.png);\n"
"padding: 0;\n"
"border: none;\n"
"background-color: rgb(250, 224, 129);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_8.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"margin: 0;\n"
"border-image: url(:/gtl_base/images/br.png);\n"
"padding: 0;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"margin: 0;\n"
"border-image: url(:/gtl_base/images/br.png);\n"
"padding: 0;\n"
"border: none;\n"
"\n"
"background-color: rgb(250, 224, 129);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 18pt \"方正舒体\";\n"
"}\n"
"QPushButton:hover{\n"
"    font: 18pt \"方正舒体\";\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 18pt \"方正舒体\";\n"
"}\n"
"QPushButton:hover{\n"
"    font: 18pt \"方正舒体\";\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 18pt \"方正舒体\";\n"
"}\n"
"QPushButton:hover{\n"
"    font: 18pt \"方正舒体\";\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 18pt \"方正舒体\";\n"
"}\n"
"QPushButton:hover{\n"
"    font: 18pt \"方正舒体\";\n"
"    color: rgb(170, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.exit_btn)
        self.pushButton.clicked.connect(Form.cp_source)
        self.pushButton_3.clicked.connect(Form.clear_text)
        self.pushButton_4.clicked.connect(Form.exit_all)
        self.pushButton_5.clicked.connect(Form.mv_tl)
        self.pushButton_6.clicked.connect(Form.mv_tr)
        self.pushButton_7.clicked.connect(Form.mv_bl)
        self.pushButton_8.clicked.connect(Form.mv_br)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.output_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文楷体\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "复制原文"))
        self.pushButton_3.setText(_translate("Form", "清空"))
        self.pushButton_4.setText(_translate("Form", "退出"))
        self.pushButton_2.setText(_translate("Form", "暂停"))
import gtl_1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
