# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 257)
        MainWindow.setMinimumSize(QtCore.QSize(421, 257))
        MainWindow.setMaximumSize(QtCore.QSize(421, 257))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 9, 401, 221))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 251, 42))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 10, 10, 10)
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.searchbtn = QtWidgets.QPushButton(self.tab_3)
        self.searchbtn.setGeometry(QtCore.QRect(290, 20, 81, 21))
        self.searchbtn.setObjectName("searchbtn")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(40, 60, 311, 121))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(19, 19, 351, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(19, 100, 351, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.showprice_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.showprice_btn.setObjectName("showprice_btn")
        self.horizontalLayout_2.addWidget(self.showprice_btn)
        self.sell_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.sell_btn.setObjectName("sell_btn")
        self.horizontalLayout_2.addWidget(self.sell_btn)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(69, 150, 261, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_9.setMinimumSize(QtCore.QSize(76, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 371, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(self.lineEdit_4.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.data = sqlite3.connect("book.db")
        self.curdata = self.data.cursor()

        self.add_btn.clicked.connect(self.add)
        self.showprice_btn.clicked.connect(self.show)
        self.sell_btn.clicked.connect(self.sell)
        self.searchbtn.clicked.connect(self.search)

    def add(self):
        bname = self.lineEdit.text().title()
        ''' Fetching the quantity and adding the addition book '''
        try:                    
            self.curdata.execute('''SELECT Bname FROM libook WHERE Bname=? ;''',(bname,))
            libook = self.curdata.fetchone()
            libook = str(libook[0])
            qtybook = self.lineEdit_4.text()
            self.curdata.execute('''SELECT quantity FROM libook WHERE Bname=?;''',(bname,))
            lqty = curdata.fetchone()
            newqty = lqty[0]+qtybook
            curdata.execute('''UPDATE libook
                                        SET quantity=?
                                        WHERE Bname=?;''',(newqty, bname,))
        except:
            
            '''Adding a whole new book with all the detail'''
            bauthor = self.lineEdit_2.text()
            bprice = self.lineEdit_3.text()
            qtybook = self.lineEdit_4.text()
            self.curdata.execute('''INSERT INTO libook(quantity, Bname, Bauthor, Bprice)
                            VALUES(?,?,?,?);''',(qtybook, bname, bauthor, bprice))
        try:
            self.data.commit()
            print("sucess")
        except:
            print("Error")
            self.data.rollback()
            
    def show(self):
        cbook =  self.lineEdit_5.text().title()
        cqty = int(self.lineEdit_7.text())
        '''fetch the quantity of the book compare the number of book taking out
            and subtract the takeout quantity from the database'''
        #try:
        self.curdata.execute('''SELECT quantity FROM libook WHERE Bname=?;''',(cbook,))
        lqty = self.curdata.fetchone()
        lqty = lqty[0]
        if cqty <= lqty:
            self.curdata.execute('''SELECT Bprice FROM libook WHERE Bname=?;''',(cbook,))
            price = self.curdata.fetchone()
            price = price[0]
            price *= cqty
            print("sucess")
            self.label_9.setText("Total price= rs"+str(price))
            
            
            
        else:
            self.label_9.text('Error! fill forms')
            
        #except:
            print("Error")
            

    def sell(self):
        cbook =  self.lineEdit_5.text().title()
        cqty = int(self.lineEdit_7.text())
        '''fetch the quantity of the book compare the number of book taking out
            and subtract the takeout quantity from the database'''
        try:
            self.curdata.execute('''SELECT quantity FROM libook WHERE Bname=?;''',(cbook,))
            lqty = self.curdata.fetchone()
            lqty = lqty[0]
            if cqty <= lqty:
                newqty = str(lqty-cqty)
                self.curdata.execute('''UPDATE libook
                                    SET quantity=?
                                    WHERE Bname=?;''',(newqty, cbook,))
                self.curdata.execute('''SELECT Bprice FROM libook WHERE Bname=?;''',(cbook,))
                price = self.curdata.fetchone()
                price = price[0]
                price *= cqty
                self.label_9.setText("Sold for rs"+str(price))
                print("sucess")
                self.data.commit()
                
            else:
                print(f'Book quantity is less than you required try small number than {lqty}: ')
            
        except:
            print("Error")
    def search(self):
        bname = self.lineEdit_6.text().title()
        try:
            ''' Fetching the quantity and adding the addition book '''                
            self.curdata.execute('''SELECT * FROM libook WHERE Bname=? ;''',(bname,))
            book_info = self.curdata.fetchone()
            book_argu = ['Quantity', 'Book Name', 'Author Name', 'Price']
            print(book_info)
            for i in range(4):
                self.model.tableView.setRow(i)
        except:
            pass           
                  
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Book Name:"))
        self.searchbtn.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Book detail"))
        self.label_5.setText(_translate("MainWindow", "Book Name:"))
        self.label_6.setText(_translate("MainWindow", "Quantity:"))
        self.showprice_btn.setText(_translate("MainWindow", "SHOW PRICE"))
        self.sell_btn.setText(_translate("MainWindow", "SELL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sell books"))
        self.label.setText(_translate("MainWindow", "Book Name:"))
        self.label_2.setText(_translate("MainWindow", "Author Name:"))
        self.label_3.setText(_translate("MainWindow", "Price:"))
        self.label_4.setText(_translate("MainWindow", "Quantity(add):"))
        self.add_btn.setText(_translate("MainWindow", "ADD"))
        self.pushButton.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add books"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
