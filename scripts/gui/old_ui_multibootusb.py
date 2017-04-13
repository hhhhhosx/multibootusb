# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/multibootusb.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(717, 516)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_usb_dev = QtWidgets.QLabel(self.groupBox_6)
        self.label_usb_dev.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usb_dev.setObjectName("label_usb_dev")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_usb_dev)
        self.usb_dev = QtWidgets.QLabel(self.groupBox_6)
        self.usb_dev.setText("")
        self.usb_dev.setObjectName("usb_dev")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usb_dev)
        self.label_usb_vendor = QtWidgets.QLabel(self.groupBox_6)
        self.label_usb_vendor.setObjectName("label_usb_vendor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_usb_vendor)
        self.usb_vendor = QtWidgets.QLabel(self.groupBox_6)
        self.usb_vendor.setText("")
        self.usb_vendor.setObjectName("usb_vendor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usb_vendor)
        self.label_usb_model = QtWidgets.QLabel(self.groupBox_6)
        self.label_usb_model.setObjectName("label_usb_model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_usb_model)
        self.label_usb_size = QtWidgets.QLabel(self.groupBox_6)
        self.label_usb_size.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_usb_size.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_usb_size.setObjectName("label_usb_size")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_usb_size)
        self.label_usb_mount = QtWidgets.QLabel(self.groupBox_6)
        self.label_usb_mount.setObjectName("label_usb_mount")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_usb_mount)
        self.usb_model = QtWidgets.QLabel(self.groupBox_6)
        self.usb_model.setText("")
        self.usb_model.setObjectName("usb_model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usb_model)
        self.usb_size = QtWidgets.QLabel(self.groupBox_6)
        self.usb_size.setText("")
        self.usb_size.setObjectName("usb_size")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usb_size)
        self.usb_mount = QtWidgets.QLabel(self.groupBox_6)
        self.usb_mount.setText("")
        self.usb_mount.setObjectName("usb_mount")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.usb_mount)
        self.gridLayout.addWidget(self.groupBox_6, 2, 0, 1, 5)
        self.close = QtWidgets.QPushButton(self.tab_3)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 9, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.browse_iso = QtWidgets.QPushButton(self.tab_3)
        self.browse_iso.setCheckable(False)
        self.browse_iso.setFlat(False)
        self.browse_iso.setObjectName("browse_iso")
        self.gridLayout.addWidget(self.browse_iso, 4, 4, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 5, 8, 2)
        self.label_persistence = QtWidgets.QLabel(self.tab_3)
        self.label_persistence.setEnabled(False)
        self.label_persistence.setMouseTracking(True)
        self.label_persistence.setStyleSheet("font-weight: 600")
        self.label_persistence.setObjectName("label_persistence")
        self.gridLayout.addWidget(self.label_persistence, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 4)
        self.detect_usb = QtWidgets.QPushButton(self.tab_3)
        self.detect_usb.setObjectName("detect_usb")
        self.gridLayout.addWidget(self.detect_usb, 1, 2, 1, 2)
        self.uninstall = QtWidgets.QPushButton(self.tab_3)
        self.uninstall.setObjectName("uninstall")
        self.gridLayout.addWidget(self.uninstall, 0, 5, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
        self.slider_persistence = QtWidgets.QSlider(self.tab_3)
        self.slider_persistence.setEnabled(False)
        self.slider_persistence.setAutoFillBackground(False)
        self.slider_persistence.setOrientation(QtCore.Qt.Horizontal)
        self.slider_persistence.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider_persistence.setObjectName("slider_persistence")
        self.gridLayout.addWidget(self.slider_persistence, 6, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 2, 1, 2)
        self.checkBox_all_drives = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_all_drives.setObjectName("checkBox_all_drives")
        self.gridLayout.addWidget(self.checkBox_all_drives, 1, 4, 1, 1)
        self.label_persistence_value = QtWidgets.QLabel(self.tab_3)
        self.label_persistence_value.setEnabled(False)
        self.label_persistence_value.setObjectName("label_persistence_value")
        self.gridLayout.addWidget(self.label_persistence_value, 6, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        self.create = QtWidgets.QPushButton(self.tab_3)
        self.create.setObjectName("create")
        self.gridLayout.addWidget(self.create, 7, 4, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 4)
        self.status = QtWidgets.QLabel(self.tab_3)
        self.status.setMinimumSize(QtCore.QSize(0, 0))
        self.status.setAcceptDrops(False)
        self.status.setAutoFillBackground(False)
        self.status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.status.setTextFormat(QtCore.Qt.AutoText)
        self.status.setScaledContents(False)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 6)
        self.labelstep1 = QtWidgets.QLabel(self.tab_3)
        self.labelstep1.setStyleSheet("font-weight: 600; margin-top:15")
        self.labelstep1.setObjectName("labelstep1")
        self.gridLayout.addWidget(self.labelstep1, 0, 0, 1, 5)
        self.labelstep2 = QtWidgets.QLabel(self.tab_3)
        self.labelstep2.setStyleSheet("font-weight: 600; margin-top:15")
        self.labelstep2.setObjectName("labelstep2")
        self.gridLayout.addWidget(self.labelstep2, 3, 0, 1, 5)
        self.labelstep3 = QtWidgets.QLabel(self.tab_3)
        self.labelstep3.setStyleSheet("font-weight: 600; margin-top:15")
        self.labelstep3.setObjectName("labelstep3")
        self.gridLayout.addWidget(self.labelstep3, 5, 0, 1, 5)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, "")
        self.imager = QtWidgets.QWidget()
        self.imager.setEnabled(True)
        self.imager.setObjectName("imager")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.imager)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.widget_7 = QtWidgets.QWidget(self.imager)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_10 = QtWidgets.QGroupBox(self.widget_7)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_9.addWidget(self.lineEdit_3)
        self.imager_bootable = QtWidgets.QLabel(self.groupBox_10)
        self.imager_bootable.setObjectName("imager_bootable")
        self.verticalLayout_9.addWidget(self.imager_bootable)
        self.imager_iso_size = QtWidgets.QLabel(self.groupBox_10)
        self.imager_iso_size.setObjectName("imager_iso_size")
        self.verticalLayout_9.addWidget(self.imager_iso_size)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.gridLayout_11.addWidget(self.groupBox_10, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget_7)
        self.groupBox_9.setStyleSheet("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_8.addWidget(self.comboBox_2)
        self.pushbtn_imager_refreshusb = QtWidgets.QPushButton(self.groupBox_9)
        self.pushbtn_imager_refreshusb.setObjectName("pushbtn_imager_refreshusb")
        self.verticalLayout_8.addWidget(self.pushbtn_imager_refreshusb)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_imager_disk_label = QtWidgets.QLabel(self.groupBox_9)
        self.label_imager_disk_label.setObjectName("label_imager_disk_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_imager_disk_label)
        self.label_imager_total_size = QtWidgets.QLabel(self.groupBox_9)
        self.label_imager_total_size.setObjectName("label_imager_total_size")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_imager_total_size)
        self.label_imager_uuid = QtWidgets.QLabel(self.groupBox_9)
        self.label_imager_uuid.setObjectName("label_imager_uuid")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_imager_uuid)
        self.imager_disk_label = QtWidgets.QLabel(self.groupBox_9)
        self.imager_disk_label.setText("")
        self.imager_disk_label.setObjectName("imager_disk_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.imager_disk_label)
        self.imager_total_size = QtWidgets.QLabel(self.groupBox_9)
        self.imager_total_size.setText("")
        self.imager_total_size.setObjectName("imager_total_size")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.imager_total_size)
        self.imager_uuid = QtWidgets.QLabel(self.groupBox_9)
        self.imager_uuid.setText("")
        self.imager_uuid.setObjectName("imager_uuid")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.imager_uuid)
        self.verticalLayout_8.addLayout(self.formLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.gridLayout_11.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_11)
        self.imager_label_status = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imager_label_status.sizePolicy().hasHeightForWidth())
        self.imager_label_status.setSizePolicy(sizePolicy)
        self.imager_label_status.setObjectName("imager_label_status")
        self.verticalLayout_6.addWidget(self.imager_label_status)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setObjectName("label_10")
        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 3)
        self.imager_progressbar = QtWidgets.QProgressBar(self.widget_7)
        self.imager_progressbar.setProperty("value", 0)
        self.imager_progressbar.setObjectName("imager_progressbar")
        self.gridLayout_12.addWidget(self.imager_progressbar, 0, 0, 1, 3)
        self.imager_write = QtWidgets.QPushButton(self.widget_7)
        self.imager_write.setObjectName("imager_write")
        self.gridLayout_12.addWidget(self.imager_write, 2, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_12)
        self.gridLayout_9.addWidget(self.widget_7, 0, 0, 1, 2)
        self.imager_close = QtWidgets.QPushButton(self.imager)
        self.imager_close.setObjectName("imager_close")
        self.gridLayout_9.addWidget(self.imager_close, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 1, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.imager, "")
        self.syslinux_ab = QtWidgets.QWidget()
        self.syslinux_ab.setObjectName("syslinux_ab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.syslinux_ab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.syslinux_ab)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.install_sys_only = QtWidgets.QRadioButton(self.groupBox_2)
        self.install_sys_only.setObjectName("install_sys_only")
        self.gridLayout_3.addWidget(self.install_sys_only, 0, 0, 1, 1)
        self.install_sys_all = QtWidgets.QRadioButton(self.groupBox_2)
        self.install_sys_all.setObjectName("install_sys_all")
        self.gridLayout_3.addWidget(self.install_sys_all, 1, 0, 1, 1)
        self.install_syslinux = QtWidgets.QPushButton(self.groupBox_2)
        self.install_syslinux.setObjectName("install_syslinux")
        self.gridLayout_3.addWidget(self.install_syslinux, 0, 2, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 1, 2, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.syslinux_ab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.edit_syslinux = QtWidgets.QPushButton(self.groupBox_3)
        self.edit_syslinux.setObjectName("edit_syslinux")
        self.gridLayout_4.addWidget(self.edit_syslinux, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem10, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.syslinux_ab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem11, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem12, 1, 6, 1, 1)
        self.boot_iso_qemu = QtWidgets.QPushButton(self.groupBox_5)
        self.boot_iso_qemu.setObjectName("boot_iso_qemu")
        self.gridLayout_7.addWidget(self.boot_iso_qemu, 3, 6, 1, 1)
        self.browse_iso_qemu = QtWidgets.QPushButton(self.groupBox_5)
        self.browse_iso_qemu.setObjectName("browse_iso_qemu")
        self.gridLayout_7.addWidget(self.browse_iso_qemu, 0, 6, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_7.addWidget(self.lineEdit_2, 0, 0, 1, 6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem13, 2, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)
        self.ram_iso_256 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_256.setObjectName("ram_iso_256")
        self.gridLayout_7.addWidget(self.ram_iso_256, 2, 1, 1, 1)
        self.ram_iso_512 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_512.setObjectName("ram_iso_512")
        self.gridLayout_7.addWidget(self.ram_iso_512, 2, 2, 1, 1)
        self.ram_iso_768 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_768.setObjectName("ram_iso_768")
        self.gridLayout_7.addWidget(self.ram_iso_768, 2, 3, 1, 1)
        self.ram_iso_1024 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_1024.setObjectName("ram_iso_1024")
        self.gridLayout_7.addWidget(self.ram_iso_1024, 2, 4, 1, 1)
        self.ram_iso_2048 = QtWidgets.QRadioButton(self.groupBox_5)
        self.ram_iso_2048.setObjectName("ram_iso_2048")
        self.gridLayout_7.addWidget(self.ram_iso_2048, 2, 5, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ram_usb_2048 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_2048.setObjectName("ram_usb_2048")
        self.gridLayout_8.addWidget(self.ram_usb_2048, 0, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem14, 0, 6, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem15, 1, 0, 1, 1)
        self.boot_usb_qemu = QtWidgets.QPushButton(self.groupBox_4)
        self.boot_usb_qemu.setObjectName("boot_usb_qemu")
        self.gridLayout_8.addWidget(self.boot_usb_qemu, 1, 6, 1, 1)
        self.ram_usb_256 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_256.setObjectName("ram_usb_256")
        self.gridLayout_8.addWidget(self.ram_usb_256, 0, 1, 1, 1)
        self.ram_usb_768 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_768.setObjectName("ram_usb_768")
        self.gridLayout_8.addWidget(self.ram_usb_768, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)
        self.ram_usb_512 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_512.setObjectName("ram_usb_512")
        self.gridLayout_8.addWidget(self.ram_usb_512, 0, 2, 1, 1)
        self.ram_usb_1024 = QtWidgets.QRadioButton(self.groupBox_4)
        self.ram_usb_1024.setObjectName("ram_usb_1024")
        self.gridLayout_8.addWidget(self.ram_usb_1024, 0, 4, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_8)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem17, 0, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem18, 1, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem19, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 1, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem20, 1, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_10)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.detect_usb)
        Dialog.setTabOrder(self.detect_usb, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.slider_persistence)
        Dialog.setTabOrder(self.slider_persistence, self.uninstall)
        Dialog.setTabOrder(self.uninstall, self.listWidget)
        Dialog.setTabOrder(self.listWidget, self.close)
        Dialog.setTabOrder(self.close, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushbtn_imager_refreshusb)
        Dialog.setTabOrder(self.pushbtn_imager_refreshusb, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.imager_write)
        Dialog.setTabOrder(self.imager_write, self.imager_close)
        Dialog.setTabOrder(self.imager_close, self.install_sys_only)
        Dialog.setTabOrder(self.install_sys_only, self.install_sys_all)
        Dialog.setTabOrder(self.install_sys_all, self.install_syslinux)
        Dialog.setTabOrder(self.install_syslinux, self.edit_syslinux)
        Dialog.setTabOrder(self.edit_syslinux, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.browse_iso_qemu)
        Dialog.setTabOrder(self.browse_iso_qemu, self.ram_iso_256)
        Dialog.setTabOrder(self.ram_iso_256, self.ram_iso_512)
        Dialog.setTabOrder(self.ram_iso_512, self.ram_iso_768)
        Dialog.setTabOrder(self.ram_iso_768, self.ram_iso_1024)
        Dialog.setTabOrder(self.ram_iso_1024, self.ram_iso_2048)
        Dialog.setTabOrder(self.ram_iso_2048, self.boot_iso_qemu)
        Dialog.setTabOrder(self.boot_iso_qemu, self.ram_usb_256)
        Dialog.setTabOrder(self.ram_usb_256, self.ram_usb_512)
        Dialog.setTabOrder(self.ram_usb_512, self.ram_usb_768)
        Dialog.setTabOrder(self.ram_usb_768, self.ram_usb_1024)
        Dialog.setTabOrder(self.ram_usb_1024, self.ram_usb_2048)
        Dialog.setTabOrder(self.ram_usb_2048, self.boot_usb_qemu)
        Dialog.setTabOrder(self.boot_usb_qemu, self.tabWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "multibootusb"))
        self.groupBox_6.setTitle(_translate("Dialog", "USB Details"))
        self.label_usb_dev.setText(_translate("Dialog", "Drive:"))
        self.label_usb_vendor.setText(_translate("Dialog", "Vendor:"))
        self.label_usb_model.setText(_translate("Dialog", "Model:"))
        self.label_usb_size.setText(_translate("Dialog", "Size:"))
        self.label_usb_mount.setText(_translate("Dialog", "Mount:"))
        self.close.setText(_translate("Dialog", "Quit"))
        self.browse_iso.setText(_translate("Dialog", "Browse ISO"))
        self.label_persistence.setText(_translate("Dialog", "Persistence"))
        self.detect_usb.setText(_translate("Dialog", "Detect Drives"))
        self.uninstall.setText(_translate("Dialog", "Uninstall Distro"))
        self.slider_persistence.setToolTip(_translate("Dialog", "Choose Persistence size. Not all distros supports persistence..."))
        self.checkBox_all_drives.setText(_translate("Dialog", "All Drives"))
        self.label_persistence_value.setText(_translate("Dialog", "0 MB"))
        self.create.setText(_translate("Dialog", "Install"))
        self.status.setText(_translate("Dialog", "Status: Idle"))
        self.labelstep1.setText(_translate("Dialog", "Step 1 :: Select drive"))
        self.labelstep2.setText(_translate("Dialog", "Step 2 :: Select ISO"))
        self.labelstep3.setText(_translate("Dialog", "Step 3 :: Install distro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "MultiBootUSB"))
        self.groupBox_10.setTitle(_translate("Dialog", "Select image"))
        self.pushButton.setText(_translate("Dialog", "Browse image..."))
        self.imager_bootable.setText(_translate("Dialog", "Bootable ISO"))
        self.imager_iso_size.setText(_translate("Dialog", "Image Size"))
        self.groupBox_9.setTitle(_translate("Dialog", "Select USB Drive"))
        self.pushbtn_imager_refreshusb.setText(_translate("Dialog", "Refresh USB"))
        self.label_imager_disk_label.setText(_translate("Dialog", "Disk Type:"))
        self.label_imager_total_size.setText(_translate("Dialog", "Disk Size:"))
        self.label_imager_uuid.setText(_translate("Dialog", "Disk Label:"))
        self.imager_label_status.setText(_translate("Dialog", "Status: Idle"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">WARNING</span> : Any bootable USB made using<span style=\" font-weight:600;\"> ISO Imager will destroy all data </span>on the selected USB disk. </p><p>Use it at your own risk. Developers are not responsile for loss of any data.</p></body></html>"))
        self.imager_write.setText(_translate("Dialog", "Write Image"))
        self.imager_close.setText(_translate("Dialog", "Quit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imager), _translate("Dialog", "Write Image to USB"))
        self.groupBox_2.setTitle(_translate("Dialog", "Install Syslinux"))
        self.install_sys_only.setText(_translate("Dialog", "Install only syslinu&x (existing configurations will not be altered)."))
        self.install_sys_all.setText(_translate("Dialog", "Install syslinux and copy all re&quired files."))
        self.install_syslinux.setText(_translate("Dialog", "Install"))
        self.groupBox_3.setTitle(_translate("Dialog", "Edit syslinux.cfg"))
        self.edit_syslinux.setText(_translate("Dialog", "Edit"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\">Edit syslinux.cfg file directly using the default editor of your system. </p><p align=\"justify\">Be <span style=\" font-weight:600; color:#ff0000;\">CAREFUL</span> while editing syslinux.cfg!</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.syslinux_ab), _translate("Dialog", "Install Syslinux"))
        self.groupBox_5.setTitle(_translate("Dialog", "Boot ISO :: Test bootable ISOs without reboot"))
        self.boot_iso_qemu.setText(_translate("Dialog", "Boot ISO"))
        self.browse_iso_qemu.setText(_translate("Dialog", "Browse ISO"))
        self.label_3.setText(_translate("Dialog", "Choose RAM size:"))
        self.ram_iso_256.setText(_translate("Dialog", "&256 MB"))
        self.ram_iso_512.setText(_translate("Dialog", "&512 MB"))
        self.ram_iso_768.setText(_translate("Dialog", "&768 MB"))
        self.ram_iso_1024.setText(_translate("Dialog", "&1024 MB"))
        self.ram_iso_2048.setText(_translate("Dialog", "204&8 MB"))
        self.groupBox_4.setTitle(_translate("Dialog", "Boot USB :: Test bootable USB drive without reboot"))
        self.ram_usb_2048.setText(_translate("Dialog", "20&48 MB"))
        self.boot_usb_qemu.setText(_translate("Dialog", "Boot USB"))
        self.ram_usb_256.setText(_translate("Dialog", "25&6 MB"))
        self.ram_usb_768.setText(_translate("Dialog", "7&68 MB"))
        self.label_4.setText(_translate("Dialog", "Choose RAM size:"))
        self.ram_usb_512.setText(_translate("Dialog", "5&12 MB"))
        self.ram_usb_1024.setText(_translate("Dialog", "1&024 MB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Boot ISO/USB"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">An advanced bootable usb creator with option to install/uninstall multiple distros.</p><p align=\"center\">This software is written in python and pyqt. </p><p align=\"center\">Copyright 2010-2016 Sundar</p><p align=\"center\"><span style=\" font-weight:600;\">Author(s)</span>: Sundar, Ian Bruce, Lee</p><p align=\"center\"><span style=\" font-weight:600;\">Licence</span>: GPL version 2 or later</p><p align=\"center\"><span style=\" font-weight:600;\">Home page</span>: <a href=\" http://multibootusb.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://multibootusb.org</span></a></p><p align=\"center\"><span style=\" font-weight:600;\">Help/Email</span>: feedback.multibootusb@gmail.com</p><p align=\"center\"><span style=\" font-weight:600;\">Source Code</span>: <a href=\"https://github.com/mbusb/multibootusb\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/mbusb/multibootusb</span></a></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "About"))

