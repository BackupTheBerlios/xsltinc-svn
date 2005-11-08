# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created: lun nov 7 20:45:52 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.14.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DemoView(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        if not name:
            self.setName("DemoView")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        DemoViewLayout = QHBoxLayout(self.centralWidget(),11,6,"DemoViewLayout")

        self.groupBox1 = QGroupBox(self.centralWidget(),"groupBox1")

        self.SourceListView = QListView(self.groupBox1,"SourceListView")
        self.SourceListView.addColumn(self.__tr("Node"))
        self.SourceListView.setGeometry(QRect(0,21,220,370))
        DemoViewLayout.addWidget(self.groupBox1)

        self.groupBox1_2_2 = QGroupBox(self.centralWidget(),"groupBox1_2_2")

        self.TransfoListView = QListView(self.groupBox1_2_2,"TransfoListView")
        self.TransfoListView.addColumn(self.__tr("Node"))
        self.TransfoListView.setGeometry(QRect(0,20,220,370))
        DemoViewLayout.addWidget(self.groupBox1_2_2)

        self.groupBox1_2 = QGroupBox(self.centralWidget(),"groupBox1_2")

        self.TargetListView = QListView(self.groupBox1_2,"TargetListView")
        self.TargetListView.addColumn(self.__tr("Node"))
        self.TargetListView.setGeometry(QRect(0,20,220,370))
        DemoViewLayout.addWidget(self.groupBox1_2)



        self.languageChange()

        self.resize(QSize(697,455).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("XsltInc demonstration"))
        self.groupBox1.setTitle(self.__tr("Source tree"))
        self.SourceListView.header().setLabel(0,self.__tr("Node"))
        self.groupBox1_2_2.setTitle(self.__tr("Transformation tree"))
        self.TransfoListView.header().setLabel(0,self.__tr("Node"))
        self.groupBox1_2.setTitle(self.__tr("Target tree"))
        self.TargetListView.header().setLabel(0,self.__tr("Node"))


    def __tr(self,s,c = None):
        return qApp.translate("DemoView",s,c)
