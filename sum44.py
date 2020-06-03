# python tkinter tutorial
# 3 main lines->3,4,6
# import tkinter
# win=tkinter.Tk() #win or root or window
# win.title("GUI")
# win.mainloop()
# from tkinter import *
# win=Tk()
# win.title("GUI")
# win.mainloop() 
import tkinter as tk
from tkinter import ttk
from csv import  DictWriter
import os
win=tk.Tk()
win.title("GUI")

# label
# widgets------->buttons,radio buttons,label---->tk,ttk(submodule)
# ttk.Label(win,text='Enter ur name : ').pack()
# pack,grid
name_label=ttk.Label(win,text='Enter ur name : ')
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter ur age : ')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='Enter ur  email : ')
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Enter ur gender : ')
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)


# create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radiobutton
# student,teacher
usertype=tk.StringVar()
radiobtr1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtr1.grid(row=4,column=0)
radiobtr2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtr2.grid(row=4,column=1)

# check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='check to subscibe to our newsletter',variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


# create a button
def action():
    user_name=name_var.get()
    user_age=age_var.get()
    user_email=email_var.get()
    print(f'{user_name} is {user_age} years old ,{user_email}')
    user_gender=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get()==0:
        subscribed='NO'
    else:
        subscribed='YES'
    print(user_gender,user_type,subscribed)
    # with open('filetk.txt','a') as f:
    #     f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed}\n')
    with open('filetk.csv','a',newline='') as f:
        dict_w=DictWriter(f,fieldnames=['username','userage','useremail','usergender','usertype','subscribed(y/n)'])
        if os.stat('filetk.csv').st_size==0:
            dict_w.writeheader()
        dict_w.writerow({
            'username':user_name,
            'userage':user_age,
            'useremail':user_email,
            'usergender':user_gender,
            'usertype':user_type,
            'subscribed(y/n)':subscribed
        })


    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#ba68c8')
    # submit_button.config(foreground='Blue')    #--->tk.Button()

submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=6, column=0)



win.mainloop() 