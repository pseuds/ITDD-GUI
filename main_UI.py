# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.openFile_Button = QtWidgets.QPushButton(self.centralwidget)
        self.openFile_Button.setStyleSheet("")
        self.openFile_Button.setObjectName("openFile_Button")
        self.horizontalLayout_8.addWidget(self.openFile_Button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.info_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.info_groupBox.setMinimumSize(QtCore.QSize(250, 0))
        self.info_groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.info_groupBox.setObjectName("info_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.info_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.info_groupBox)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(self.info_groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.imageSizeInfo_label = QtWidgets.QLabel(self.info_groupBox)
        self.imageSizeInfo_label.setObjectName("imageSizeInfo_label")
        self.horizontalLayout_11.addWidget(self.imageSizeInfo_label)
        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.info_groupBox)
        self.predictParams_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.predictParams_groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.predictParams_groupBox.setObjectName("predictParams_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.predictParams_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.predictParams_groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minConf_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.minConf_label.setObjectName("minConf_label")
        self.horizontalLayout_2.addWidget(self.minConf_label)
        self.conf_Slider = QtWidgets.QSlider(self.predictParams_groupBox)
        self.conf_Slider.setMaximumSize(QtCore.QSize(16777215, 20))
        self.conf_Slider.setMinimum(1)
        self.conf_Slider.setMaximum(100)
        self.conf_Slider.setSingleStep(1)
        self.conf_Slider.setPageStep(10)
        self.conf_Slider.setSliderPosition(50)
        self.conf_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.conf_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.conf_Slider.setTickInterval(10)
        self.conf_Slider.setObjectName("conf_Slider")
        self.horizontalLayout_2.addWidget(self.conf_Slider)
        self.maxConf_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.maxConf_label.setObjectName("maxConf_label")
        self.horizontalLayout_2.addWidget(self.maxConf_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.confValue_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.confValue_label.setObjectName("confValue_label")
        self.horizontalLayout.addWidget(self.confValue_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.predictParams_groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minIoU_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.minIoU_label.setObjectName("minIoU_label")
        self.horizontalLayout_5.addWidget(self.minIoU_label)
        self.IoU_Slider = QtWidgets.QSlider(self.predictParams_groupBox)
        self.IoU_Slider.setMaximumSize(QtCore.QSize(16777215, 20))
        self.IoU_Slider.setMinimum(1)
        self.IoU_Slider.setMaximum(100)
        self.IoU_Slider.setSingleStep(1)
        self.IoU_Slider.setPageStep(10)
        self.IoU_Slider.setSliderPosition(50)
        self.IoU_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.IoU_Slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.IoU_Slider.setTickInterval(10)
        self.IoU_Slider.setObjectName("IoU_Slider")
        self.horizontalLayout_5.addWidget(self.IoU_Slider)
        self.maxIoU_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.maxIoU_label.setObjectName("maxIoU_label")
        self.horizontalLayout_5.addWidget(self.maxIoU_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.iouValue_label = QtWidgets.QLabel(self.predictParams_groupBox)
        self.iouValue_label.setObjectName("iouValue_label")
        self.horizontalLayout_6.addWidget(self.iouValue_label)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.predictParams_groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.imageSize_spinBox = QtWidgets.QSpinBox(self.predictParams_groupBox)
        self.imageSize_spinBox.setMinimum(400)
        self.imageSize_spinBox.setMaximum(1280)
        self.imageSize_spinBox.setProperty("value", 800)
        self.imageSize_spinBox.setObjectName("imageSize_spinBox")
        self.horizontalLayout_7.addWidget(self.imageSize_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_3 = QtWidgets.QLabel(self.predictParams_groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        self.maxDet_spinBox = QtWidgets.QSpinBox(self.predictParams_groupBox)
        self.maxDet_spinBox.setMinimum(1)
        self.maxDet_spinBox.setMaximum(300)
        self.maxDet_spinBox.setProperty("value", 300)
        self.maxDet_spinBox.setObjectName("maxDet_spinBox")
        self.horizontalLayout_15.addWidget(self.maxDet_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.verticalLayout_6.addWidget(self.predictParams_groupBox)
        self.displayOptions_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.displayOptions_groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.displayOptions_groupBox.setObjectName("displayOptions_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.displayOptions_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preprocess_checkBox = QtWidgets.QCheckBox(self.displayOptions_groupBox)
        self.preprocess_checkBox.setObjectName("preprocess_checkBox")
        self.verticalLayout_2.addWidget(self.preprocess_checkBox)
        self.hideBoxes_checkBox = QtWidgets.QCheckBox(self.displayOptions_groupBox)
        self.hideBoxes_checkBox.setObjectName("hideBoxes_checkBox")
        self.verticalLayout_2.addWidget(self.hideBoxes_checkBox)
        self.hideLabels_checkBox = QtWidgets.QCheckBox(self.displayOptions_groupBox)
        self.hideLabels_checkBox.setObjectName("hideLabels_checkBox")
        self.verticalLayout_2.addWidget(self.hideLabels_checkBox)
        self.hideConf_checkBox = QtWidgets.QCheckBox(self.displayOptions_groupBox)
        self.hideConf_checkBox.setObjectName("hideConf_checkBox")
        self.verticalLayout_2.addWidget(self.hideConf_checkBox)
        self.verticalLayout_6.addWidget(self.displayOptions_groupBox)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.predict_Button = QtWidgets.QPushButton(self.centralwidget)
        self.predict_Button.setStyleSheet("")
        self.predict_Button.setObjectName("predict_Button")
        self.horizontalLayout_12.addWidget(self.predict_Button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.video_label = QtWidgets.QLabel(self.page)
        self.video_label.setObjectName("video_label")
        self.gridLayout_4.addWidget(self.video_label, 0, 0, 1, 1)
        self.video_Slider = QtWidgets.QSlider(self.page)
        self.video_Slider.setMaximumSize(QtCore.QSize(16777215, 15))
        self.video_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.video_Slider.setObjectName("video_Slider")
        self.gridLayout_4.addWidget(self.video_Slider, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.photo_label = QtWidgets.QLabel(self.page_2)
        self.photo_label.setMinimumSize(QtCore.QSize(600, 0))
        self.photo_label.setMaximumSize(QtCore.QSize(800, 16777215))
        self.photo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_label.setObjectName("photo_label")
        self.gridLayout_5.addWidget(self.photo_label, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem13, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_10.addWidget(self.stackedWidget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.classes_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.classes_groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.classes_groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.classes_groupBox.setObjectName("classes_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.classes_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.classes_groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 278, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.result_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)
        self.gridLayout_3.addWidget(self.result_table, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.saveTable_Button = QtWidgets.QPushButton(self.classes_groupBox)
        self.saveTable_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.saveTable_Button.setObjectName("saveTable_Button")
        self.horizontalLayout_14.addWidget(self.saveTable_Button)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 4, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_4 = QtWidgets.QLabel(self.classes_groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_16.addWidget(self.label_4)
        self.sortClass_Button = QtWidgets.QPushButton(self.classes_groupBox)
        self.sortClass_Button.setObjectName("sortClass_Button")
        self.horizontalLayout_16.addWidget(self.sortClass_Button)
        self.sortConf_Button = QtWidgets.QPushButton(self.classes_groupBox)
        self.sortConf_Button.setObjectName("sortConf_Button")
        self.horizontalLayout_16.addWidget(self.sortConf_Button)
        self.gridLayout_2.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.classes_groupBox)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.viewOriginal_Button = QtWidgets.QPushButton(self.centralwidget)
        self.viewOriginal_Button.setObjectName("viewOriginal_Button")
        self.horizontalLayout_13.addWidget(self.viewOriginal_Button)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem17)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.saveFile_Button = QtWidgets.QPushButton(self.centralwidget)
        self.saveFile_Button.setStyleSheet("")
        self.saveFile_Button.setObjectName("saveFile_Button")
        self.horizontalLayout_9.addWidget(self.saveFile_Button)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detection of Interlocking Tiles Defects"))
        self.openFile_Button.setText(_translate("MainWindow", "Open File"))
        self.info_groupBox.setTitle(_translate("MainWindow", "Info"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>This model was trained using <span style=\" font-weight:600;\">YOLOv8</span> with image size <span style=\" font-weight:600;\">800px</span>, trained with the following classes:</p><p>interlocking tiles, repair tiles, asphalt, manhole, road marking (fade), road marking (good)</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Imported image size:"))
        self.imageSizeInfo_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">  - </span></p></body></html>"))
        self.predictParams_groupBox.setTitle(_translate("MainWindow", "Prediction Parameters"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Object Confidence Threshold</span></p></body></html>"))
        self.minConf_label.setText(_translate("MainWindow", "   1"))
        self.maxConf_label.setText(_translate("MainWindow", "100"))
        self.confValue_label.setText(_translate("MainWindow", "50"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Intersection over Confidence (IoU)</span></p></body></html>"))
        self.minIoU_label.setText(_translate("MainWindow", "   1"))
        self.maxIoU_label.setText(_translate("MainWindow", "100"))
        self.iouValue_label.setText(_translate("MainWindow", "50"))
        self.label_11.setText(_translate("MainWindow", "Image size"))
        self.label_3.setText(_translate("MainWindow", "Max no. of detections"))
        self.displayOptions_groupBox.setTitle(_translate("MainWindow", "Display Options"))
        self.preprocess_checkBox.setText(_translate("MainWindow", "Preprocess"))
        self.hideBoxes_checkBox.setText(_translate("MainWindow", "Hide boxes"))
        self.hideLabels_checkBox.setText(_translate("MainWindow", "Hide labels"))
        self.hideConf_checkBox.setText(_translate("MainWindow", "Hide Confidence Scores"))
        self.predict_Button.setText(_translate("MainWindow", "Predict"))
        self.video_label.setText(_translate("MainWindow", "TextLabel"))
        self.photo_label.setText(_translate("MainWindow", "TextLabel"))
        self.classes_groupBox.setTitle(_translate("MainWindow", "Classes"))
        self.saveTable_Button.setText(_translate("MainWindow", "Save Table"))
        self.label_4.setText(_translate("MainWindow", "Sort by:"))
        self.sortClass_Button.setText(_translate("MainWindow", "Class"))
        self.sortConf_Button.setText(_translate("MainWindow", "Confidence"))
        self.viewOriginal_Button.setText(_translate("MainWindow", "View Original"))
        self.saveFile_Button.setText(_translate("MainWindow", "Save File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())