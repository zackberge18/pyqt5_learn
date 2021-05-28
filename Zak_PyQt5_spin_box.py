import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #title
        self.setWindowTitle("Rana")
        #set layout vertically
        self.setLayout(qtw.QVBoxLayout())
        #create a label
        self.my_label=qtw.QLabel("Hello Cruel world")
        #Change font size of label
        self.my_label.setFont(qtg.QFont("Papyrus",20))
        self.layout().addWidget(self.my_label)

        #create combo box
        self.my_spin=qtw.QDoubleSpinBox(self,
            value=1,
            maximum=100,
            minimum=0,
            singleStep=3.33,prefix="#",suffix="order")

        self.layout().addWidget(self.my_spin)
        self.my_spin.setFont((qtg.QFont("Papyrus",20)))


        #crate a button
        self.my_button=qtw.QPushButton("Press me",
                clicked=lambda :self.press_it())
        self.my_button.setFont(qtg.QFont("Papyrus",30))
        self.layout().addWidget(self.my_button)






        # dont know but that make it work
        self.show()

    def press_it(self):
        self.my_label.setText(f"you picked {round(float(self.my_spin.value()),4)} !!!\n")




app=qtw.QApplication([])
mw=MainWindow()


#run the app
app.exec_()