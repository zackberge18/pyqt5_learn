

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.QtCore import QTime,QTimer


class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        #add title
        self.setWindowTitle("my threading")

        #Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #create label
        my_label=qtw.QLabel("YOur name")
        my_label.setFont(qtg.QFont("Papyrus",20))
        self.layout().addWidget(my_label)

        #create a entry
        self.my_enty=qtw.QLineEdit()
        self.my_enty.setText("Zack")
        self.layout().addWidget(self.my_enty)

        #create a button
        my_button=qtw.QPushButton("pRess Me",clicked=self.press_it)
        self.layout().addWidget(my_button)

        self.show()
    def press_it(self):


            alien=self.my_enty.text()
            # creating a timer object
            timer = QTimer(self)
            # adding action to timer
            timer.timeout.connect(lambda : self.showTime(alien))

            # update the timer every second
            timer.start(1000)
            self.count = 0
            self.f = ""


    def showTime(self,be):
        try:
            l_show=be[self.count]

            self.f=self.f+" "+l_show
            #delete a label
            if self.count==0:
                # create label
                self.ch_label = qtw.QLabel(f"{str(self.f)}")
                self.ch_label.setFont(qtg.QFont("Papyrus", 20))
                self.layout().addWidget(self.ch_label)
            else:
                self.ch_label.setText(f"{str(self.f)}")
            self.count += 1

        except :
            pass



app=qtw.QApplication([])
mw=MainWindow()

app.exec_()