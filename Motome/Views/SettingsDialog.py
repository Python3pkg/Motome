# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Motome\Views\SettingsDialog.ui'
#
# Created: Fri Mar 14 15:48:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SettingsDialog.resize(578, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/resources/logo_320x320.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsDialog.setWindowIcon(icon)
        SettingsDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.conf_notesLocation = QtGui.QLineEdit(self.tab)
        self.conf_notesLocation.setObjectName("conf_notesLocation")
        self.horizontalLayout.addWidget(self.conf_notesLocation)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.conf_author = QtGui.QLineEdit(self.tab)
        self.conf_author.setObjectName("conf_author")
        self.horizontalLayout_2.addWidget(self.conf_author)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.conf_checkbox_firstlinetitle = QtGui.QCheckBox(self.tab)
        self.conf_checkbox_firstlinetitle.setChecked(True)
        self.conf_checkbox_firstlinetitle.setObjectName("conf_checkbox_firstlinetitle")
        self.verticalLayout.addWidget(self.conf_checkbox_firstlinetitle)
        self.conf_checkbox_titleasfilename = QtGui.QCheckBox(self.tab)
        self.conf_checkbox_titleasfilename.setChecked(True)
        self.conf_checkbox_titleasfilename.setObjectName("conf_checkbox_titleasfilename")
        self.verticalLayout.addWidget(self.conf_checkbox_titleasfilename)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.conf_checkbox_recordonsave = QtGui.QCheckBox(self.tab)
        self.conf_checkbox_recordonsave.setChecked(True)
        self.conf_checkbox_recordonsave.setObjectName("conf_checkbox_recordonsave")
        self.verticalLayout.addWidget(self.conf_checkbox_recordonsave)
        self.conf_checkbox_recordonswitch = QtGui.QCheckBox(self.tab)
        self.conf_checkbox_recordonswitch.setChecked(True)
        self.conf_checkbox_recordonswitch.setObjectName("conf_checkbox_recordonswitch")
        self.verticalLayout.addWidget(self.conf_checkbox_recordonswitch)
        self.conf_checkbox_recordonexit = QtGui.QCheckBox(self.tab)
        self.conf_checkbox_recordonexit.setChecked(True)
        self.conf_checkbox_recordonexit.setObjectName("conf_checkbox_recordonexit")
        self.verticalLayout.addWidget(self.conf_checkbox_recordonexit)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.about_version_label = QtGui.QLabel(self.tab)
        self.about_version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.about_version_label.setObjectName("about_version_label")
        self.verticalLayout.addWidget(self.about_version_label)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.textMarkdownHelp = QtGui.QTextBrowser(self.tab_3)
        self.textMarkdownHelp.setReadOnly(True)
        self.textMarkdownHelp.setAcceptRichText(False)
        self.textMarkdownHelp.setSource(QtCore.QUrl("qrc:/html/resources/markdown_help.html"))
        self.textMarkdownHelp.setObjectName("textMarkdownHelp")
        self.verticalLayout_4.addWidget(self.textMarkdownHelp)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textShorcutsHelp = QtGui.QTextBrowser(self.tab_4)
        self.textShorcutsHelp.setSource(QtCore.QUrl("qrc:/html/resources/keyboard_shortcuts.html"))
        self.textShorcutsHelp.setObjectName("textShorcutsHelp")
        self.verticalLayout_5.addWidget(self.textShorcutsHelp)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textAboutHelp = QtGui.QTextBrowser(self.tab_2)
        self.textAboutHelp.setSource(QtCore.QUrl("qrc:/html/resources/about.html"))
        self.textAboutHelp.setOpenExternalLinks(True)
        self.textAboutHelp.setOpenLinks(False)
        self.textAboutHelp.setObjectName("textAboutHelp")
        self.verticalLayout_3.addWidget(self.textAboutHelp)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), SettingsDialog.load_folder_location)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "Notes location", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_notesLocation.setPlaceholderText(QtGui.QApplication.translate("SettingsDialog", "Required - Please select a notes location...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SettingsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_author.setToolTip(QtGui.QApplication.translate("SettingsDialog", "Chijiiwa Motome <cmotome@example.com>", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_author.setPlaceholderText(QtGui.QApplication.translate("SettingsDialog", "Optional - Please enter your name", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_checkbox_firstlinetitle.setText(QtGui.QApplication.translate("SettingsDialog", "Use the first  line of the note as the title", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_checkbox_titleasfilename.setText(QtGui.QApplication.translate("SettingsDialog", "Set the note title as the file name", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_checkbox_recordonsave.setText(QtGui.QApplication.translate("SettingsDialog", "Record note data to version history with Ctrl/Cmd-S", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_checkbox_recordonswitch.setText(QtGui.QApplication.translate("SettingsDialog", "Record changed note data to version history when switching notes", None, QtGui.QApplication.UnicodeUTF8))
        self.conf_checkbox_recordonexit.setText(QtGui.QApplication.translate("SettingsDialog", "Record changed note data to version history on exit", None, QtGui.QApplication.UnicodeUTF8))
        self.about_version_label.setText(QtGui.QApplication.translate("SettingsDialog", "v0.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "<html><head/><body><p><a href=\"http://daringfireball.net/projects/markdown/syntax\"><span style=\" text-decoration: underline; color:#0000ff;\">See official syntax for details</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("SettingsDialog", "Markdown Help", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("SettingsDialog", "Keyboard Shortcuts", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("SettingsDialog", "About", None, QtGui.QApplication.UnicodeUTF8))

import MainWindow_rc
