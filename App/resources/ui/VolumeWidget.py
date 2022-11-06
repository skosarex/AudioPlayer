# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VolumeWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VolumeWidget(object):
    def setupUi(self, VolumeWidget):
        VolumeWidget.setObjectName("VolumeWidget")
        VolumeWidget.resize(420, 70)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("App/resources/icons/volume_black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VolumeWidget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(VolumeWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.volume_slider = QtWidgets.QSlider(VolumeWidget)
        self.volume_slider.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
                                         "gridline-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(255, 255, 255);")
        self.volume_slider.setSliderPosition(99)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout_2.addWidget(self.volume_slider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #
        self.volume_slider.setStyleSheet("""
                                    QSlider::groove:horizontal {  
                                        height: 6px;
                                        margin: 0px;
                                        border-radius: 3px;
                                        background: #B0AEB1;
                                    }
                                    QSlider::handle:horizontal {
                                        background: #fff;
                                        border: 1px solid #fff;
                                        width: 10px;
                                        margin: -5px 0; 
                                        border-radius: 5px;
                                    }
                                    QSlider::sub-page:qlineargradient {
                                        background: #fff;
                                        border-radius: 3px;
                                    }
                                """)
        #

        self.retranslateUi(VolumeWidget)
        QtCore.QMetaObject.connectSlotsByName(VolumeWidget)

    def retranslateUi(self, VolumeWidget):
        _translate = QtCore.QCoreApplication.translate
        VolumeWidget.setWindowTitle(_translate("VolumeWidget", "Volume"))
