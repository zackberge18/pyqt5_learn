from tkinter import *
from tkinter import ttk
import sqlite3
import os
import datetime
import time
class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("500x550")
        #create an icon
        #create a title
        #create a platforms
        self.platforms_notebook=ttk.Notebook(self)
        self.platforms_notebook.pack(pady=15,padx=3)
        #Create COOK AND STUDENT platform
        self.cook_frame=Frame(self.platforms_notebook,width=500,height=500,bg="green")
        self.student_frame = Frame(self.platforms_notebook, width=500, height=500, bg="red")
        self.exist_food_frame=Frame(self.platforms_notebook, width=500, height=500)
        self.cook_frame.pack(fill=BOTH,expand=1)
        self.student_frame.pack(fill=BOTH, expand=1)
        self.exist_food_frame.pack(fill=BOTH, expand=1)
        #create cook and student Platform
        self.platforms_notebook.add(self.cook_frame,text="COOK")
        self.platforms_notebook.add(self.student_frame, text="STUDENT")
        self.platforms_notebook.add(self.exist_food_frame, text="FOOD")

        ####for cook platform
            ## use Grid system
            ##use cook_frame
            ## Create label and button for name of cokker
        self.cook_name_label=Label(self.cook_frame,text="Name",fg="orange",width=10)
        self.cook_name_label.grid(row=1,column=0)
        self.cook_name_entry=Entry(self.cook_frame,width=60)
        self.cook_name_entry.grid(row=1,column=1)
            ## Create a text widget for food and first line should be name
        self.cook_text=Text(self.cook_frame,width=60,height=27)
        self.cook_text.grid(row=2,column=0,columnspan=2)
            ## text widget rest will be about dish
            ## send all info inside text widget to db
        self.cook_button=Button(self.cook_frame,text="publish",command=self.cook_db_it)
        self.cook_button.grid(row=3,column=1)
        # Create Existing Food for The day
        # use grid system
        try:
            # use exist_food_frame
            conn = sqlite3.connect("cook.db")
            c = conn.cursor()
            c.execute("SELECT * FROM cook")
            cook_records = c.fetchall()
            conn.commit()
            conn.close()


            self.test_label = Label(self.exist_food_frame, text=cook_records[0][1], font="arial 10 bold",width=30)
            self.test_label.grid(row=0, column=0)
            self.test_info_button = Button(self.exist_food_frame, text="See more",padx=20,command=self.see_more)
            self.test_info_button.grid(row=0, column=1)
            # create 10 hour timer
            self.test_timer_label = Label(self.exist_food_frame, text="10:60:60",width=30)
            self.test_timer_label.grid(row=0, column=2)
            self.test_timer_label.after(1000,self.countdown)
        except:
            pass
        #
        # Create Wish food AND STUDENT PLATFORM
        #USE student_frame
        student_label=Label(self.student_frame,text="name")
        student_label.grid(row=0,column=0,padx=10,pady=10)
        student_list_box=Listbox(self.student_frame)
        student_list_box.grid(row=1,column=1)
        conn = sqlite3.connect("cook.db")
        c = conn.cursor()

        c.execute('SELECT * FROM cook')
        student_for_databe=c.fetchall()
        conn.commit()
        conn.close()
        for i in student_for_databe:
            student_list_box.insert(END,i[1])
        self.werde=student_list_box.get(ACTIVE)
        claim_button=Button(self.student_frame,text="claim",command=self.claim)
        claim_button.grid(row=2,column=0)

    def claim(self):
        myLabel_for_purchase=Label(self.student_frame,text=self.werde+" IS PLACED AAN ORDER",width=30)
        myLabel_for_purchase.grid(row=3,column=2)





        # create Commnet section for food and

        #func for db
    def cook_db_it(self):
        self.cook_name=self.cook_name_entry.get()
        self.dish_name=self.cook_text.get(1.0,2.0)
        self.dish_info=self.cook_text.get(3.0,END)
            #create A database
        conn=sqlite3.connect("cook.db")
        c=conn.cursor()

        c.execute('INSERT INTO cook VALUES(:cook_name,:dish_name,:dish_info)',{"cook_name":self.cook_name,"dish_name":self.dish_name,"dish_info":self.dish_info})
        conn.commit()
        conn.close()
    def countdown(self):

            hour=time.strftime("%H")
            mins=time.strftime("%M")
            secs=time.strftime("%S")
            timer = f'{hour}:{mins}:{secs}'
            self.test_timer_label.config(text=timer)
            self.test_timer_label.after(1000, self.countdown)

    def see_more(self):
        conn = sqlite3.connect("cook.db")
        c = conn.cursor()
        c.execute("SELECT * FROM cook")
        cook_records = c.fetchall()
        conn.commit()
        conn.close()
        top_frame=Toplevel(self)
        Label(top_frame,text="name  "+cook_records[0][0],font="arial 30 bold").pack()
        Label(top_frame, text="food name  " + cook_records[0][1], font="arial 30 bold").pack()
        Label(top_frame, text="recipe  " + cook_records[0][2], font="arial 30 bold").pack()





if __name__ == '__main__':
    app=App()
    app.mainloop()