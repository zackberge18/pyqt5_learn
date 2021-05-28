import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow (qtw.QWidget) :
    def __init__(self):
        super(MainWindow, self).__init__()
        #add title
        self.setWindowTitle("hello world")

        #set Vertical layout
        #self.setLayout(qtw.QVBoxLayout())
        form_layout=qtw.QFormLayout()
        self.setLayout(form_layout)

        ##add widget /stuff

        self.label_1=qtw.QLabel("this is a cool label")
        self.label_1.setFont(qtg.QFont("Papyrus",20))
        self.f_name=qtw.QLineEdit(self)
        self.l_name=qtw.QLineEdit(self)


        #add Rows to app
        form_layout.addRow(self.label_1)
        form_layout.addRow("First name :",self.f_name)
        form_layout.addRow("last name :",self.l_name)
        form_layout.addRow(qtw.QPushButton("press me",
      clicked=lambda : self.press_it()))


        #show the app
        self.show()
    def press_it(self):
        self.label_1.setText(f"you clicked {self.f_name.text()} and {self.l_name.text()}")




app=qtw.QApplication([])
mw= MainWindow()

#run the app
app.exec_()
