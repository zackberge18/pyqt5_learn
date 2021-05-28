import PyQt5.QtWidgets as qtW
import PyQt5.QtGui as qtG
import numpy as np

class MainWindow(qtW.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # title
        self.setWindowTitle("Rana")
        # set layout vertically
        self.setLayout(qtW.QVBoxLayout())
        # create a label
        self.my_label = qtW.QLabel("Hello Cruel world")
        # Change font size of label
        self.my_label.setFont(qtG.QFont("Papyrus", 20))
        self.layout().addWidget(self.my_label)

        # create combo box
        self.my_combo = qtW.QComboBox(self)
        my_list = np.random.randint(100, size=5)
        for i in my_list:
            self.my_combo.addItem(str(i))
        self.layout().addWidget(self.my_combo)


        # crate a button
        self.my_button = qtW.QPushButton("Press me",
                                       clicked=lambda :self.press_it())
        self.my_button.setFont(qtG.QFont("Papyrus", 30))
        self.layout().addWidget(self.my_button)






        # dont know but that make it work
        self.show()

    def press_it(self):
        self.my_label.setText(f"you picked {self.my_combo.currentText()} !!!\n")





app = qtW.QApplication([])
mw = MainWindow()


# run the app
app.exec_()