
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


#create or connect to one
conn=sqlite3.connect("mylist.db")
#create a cursor farmer
c=conn.cursor()

#create a table
c.execute(("""CREATE TABLE if not exists todo_list(
    list_item text
)"""))
conn.commit()
conn.close()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 562)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_b = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.my_func(1))
        self.add_b.setGeometry(QtCore.QRect(32, 80, 81, 51))
        self.add_b.setObjectName("add_b")
        self.del_b = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.my_func(2))
        self.del_b.setGeometry(QtCore.QRect(140, 80, 103, 51))
        self.del_b.setObjectName("del_b")
        self.clear_b = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.my_func(3))
        self.clear_b.setGeometry(QtCore.QRect(270, 80, 91, 51))
        self.clear_b.setObjectName("clear_b")
        self.line_item = QtWidgets.QLineEdit(self.centralwidget)
        self.line_item.setGeometry(QtCore.QRect(22, 10, 471, 41))
        self.line_item.setObjectName("line_item")
        self.list_item = QtWidgets.QListWidget(self.centralwidget)
        self.list_item.setGeometry(QtCore.QRect(30, 140, 331, 361))
        self.list_item.setObjectName("list_item")
        self.save_b = QtWidgets.QPushButton(self.centralwidget,clicked=lambda :self.save_func())
        self.save_b.setGeometry(QtCore.QRect(370, 270, 91, 51))
        self.save_b.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.save_b.setAutoFillBackground(False)
        self.save_b.setObjectName("save_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #grap all from data base
        self.grap_all()
    def grap_all(self):
        # create or connect to one
        conn = sqlite3.connect("mylist.db")
        # create a cursor farmer
        c = conn.cursor()

        # create a table
        c.execute(("SELECT * FROM todo_list"))
        records=c.fetchall()
        conn.commit()
        conn.close()
        for record in records:
            self.list_item.addItem(str(record[0]))



    def my_func(self, x):
            ##Add item
            if x == 1:
                # grap item from list box
                item = self.line_item.text()
                # add item to list box
                self.list_item.addItem(item)
                self.line_item.setText(" ")
            # delete it
            elif x == 2:

                clicked = self.list_item.currentRow()
                self.list_item.takeItem(clicked)
            # clear item
            else:
                self.line_item.setText(" ")
    def save_func(self):
        # create or connect to one
        conn = sqlite3.connect("mylist.db")
        # create a cursor farmer
        c = conn.cursor()

        # DELETE EVERYTHING ALL
        c.execute("DELETE FROM todo_list;")



        #create blank list
        items=[]
        # through list item
        for index in range(self.list_item.count()):
            items.append(self.list_item.item(index))
        for item in items:
            #print(item.text())
            c.execute("INSERT INTO todo_list VALUES (:item)",{"item":item.text()})
        conn.commit()
        conn.close()

        #Pop up box
        msg=QMessageBox()
        msg.setWindowTitle("saved to database")
        msg.setIcon(QMessageBox.Information)
        msg.setText("your todo list has been saved")

        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_b.setText(_translate("MainWindow", "Add"))
        self.del_b.setText(_translate("MainWindow", "Delete"))
        self.clear_b.setText(_translate("MainWindow", "Clear"))
        self.save_b.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
