#admin signup GUI

from tkinter import *
import tkinter.messagebox
import empinfo

root = Tk()
root.title('Create new Admin')
##
#fetches data from GUI and creates new Admin 
def fetch():
    if(entry_3s.get()=="1234"):#software key *************** 
            #empinfo.signup(entry_1s.get(),entry_2s.get(),entry_4s.get())
            empinfo.signup(entry_1s.get(),entry_2s.get())#without email
            tkinter.messagebox.showinfo("Updated","New Admin Created")
            entry_1s.delete(0, END)
            entry_2s.delete(0, END)
            entry_3s.delete(0, END)
    else:
            tkinter.messagebox.showinfo("Wrong Key","Please enter valid software key")
            entry_3s.delete(0, END)
            
    

# all GUI
admin_login_label=Label(root,text="Please Enter details  ")
admin_login_label.grid(row=0,columnspan=2)
admin_login_label.config(bg='grey', fg='white')


label_1s=Label(root,text="ID")
entry_1s=Entry(root)

label_1s.grid(row=1,sticky=E)#use north south N S with sticky
entry_1s.grid(row=1,column=1)


label_2s=Label(root,text="Password")
entry_2s=Entry(root)

label_2s.grid(row=2,sticky=E)#use north south N S with sticky
entry_2s.grid(row=2,column=1)


label_3s=Label(root,text="Software Key")
entry_3s=Entry(root)

label_3s.grid(row=4,sticky=E)#use north south N S with sticky
entry_3s.grid(row=4,column=1)
''' 
#EMAIL PART
label_4s=Label(root,text="Email ID")
entry_4s=Entry(root)

label_4s.grid(row=3,sticky=E)#use north south N S with sticky
entry_4s.grid(row=3,column=1)
'''
button_submits=Button(root, text="Submit",fg='green',command=fetch)
button_submits.grid(row=5,columnspan=2)






root.mainloop()
