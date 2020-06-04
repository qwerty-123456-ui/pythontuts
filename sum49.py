import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()

# label frame
label_frame=ttk.LabelFrame(win,text='Enter ur contacts')
label_frame.grid(row=0,column=0,padx=40,pady=10)

name_label=ttk.Label(label_frame,text='Enter ur name',font=('Helvetica',14,'bold'))
age_label=ttk.Label(label_frame,text='Enter ur age',font=('Helvetica',14,'bold'))

name_var=tk.StringVar()
age_var=tk.StringVar()

name_entry=ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=36,textvariable=age_var)

name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    # m_box.showinfo('title','content of this message box!!!!')
    # m_box.showerror('title','content of this message box!!!!')
    # m_box.showwarning('title','content of this message box!!!!')
    name=name_var.get()
    age=age_var.get()
    if name=='' or age=='':
        m_box.showerror('Error','Please fill both name and age')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('Error','Only digits are allowed')
        else:
            if age<18:
                m_box.showwarning('warning','ur not 18, visit this content on ur risk')
            print(f"{name} : {age}")
submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)

win.mainloop()