# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created: mar nov 8 19:15:37 2005
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
        self.groupBox1.setColumnLayout(0,Qt.Vertical)
        self.groupBox1.layout().setSpacing(6)
        self.groupBox1.layout().setMargin(11)
        groupBox1Layout = QHBoxLayout(self.groupBox1.layout())
        groupBox1Layout.setAlignment(Qt.AlignTop)

        self.SourceListView = QListView(self.groupBox1,"SourceListView")
        self.SourceListView.addColumn(self.__tr("Node"))
        self.SourceListView.setAcceptDrops(1)
        groupBox1Layout.addWidget(self.SourceListView)
        DemoViewLayout.addWidget(self.groupBox1)

        self.groupBox1_2_2 = QGroupBox(self.centralWidget(),"groupBox1_2_2")
        self.groupBox1_2_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_2_2.layout().setSpacing(6)
        self.groupBox1_2_2.layout().setMargin(11)
        groupBox1_2_2Layout = QHBoxLayout(self.groupBox1_2_2.layout())
        groupBox1_2_2Layout.setAlignment(Qt.AlignTop)

        self.TransfoListView = QListView(self.groupBox1_2_2,"TransfoListView")
        self.TransfoListView.addColumn(self.__tr("Node"))
        self.TransfoListView.setAcceptDrops(1)
        groupBox1_2_2Layout.addWidget(self.TransfoListView)
        DemoViewLayout.addWidget(self.groupBox1_2_2)

        self.groupBox1_2 = QGroupBox(self.centralWidget(),"groupBox1_2")
        self.groupBox1_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox1_2.layout().setSpacing(6)
        self.groupBox1_2.layout().setMargin(11)
        groupBox1_2Layout = QHBoxLayout(self.groupBox1_2.layout())
        groupBox1_2Layout.setAlignment(Qt.AlignTop)

        self.TargetListView = QListView(self.groupBox1_2,"TargetListView")
        self.TargetListView.addColumn(self.__tr("Node"))
        self.TargetListView.setAcceptDrops(1)
        groupBox1_2Layout.addWidget(self.TargetListView)
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
