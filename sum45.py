# for loop
import tkinter as tk
from tkinter import ttk
win =tk.Tk()
win.title('LOOP')
labels=["What is ur name ? ","What is ur age ? ","What is ur gender ? ","Country","State","City"]
# name_label=ttk.Label(win,text="Enter ur name")
# name_label.grid(row=0,column=0,sticky=tk.W)

for i in range(len(labels)):
    cur_label='label'+str(i)
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)

# entry box
# nam_var=tk.StringVar()
# name_entry=ttk.Entry(win,width=16,textvariable=nam_var)
# name_entry.grid(row=0,column=1)

user_info={
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
    }
counter=0
for i in user_info:
    cur_entrybox='entry_'+i
    cur_entrybox=ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1,padx=2,pady=2)
    counter+=1
    
def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info['gender'].get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())

submit_btn=ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=6,columnspan=2)

win.mainloop()