# Main GUI
from tkinter import * 
import tkinter.messagebox
import empinfo
import sendmail
from pro_face_recog.run import *
root=Tk()

topFrame= Frame(root)
topFrame.grid(row=0,column=0)

adminFrame= Frame(root)
updateFrame=Frame(root)
deleteFrame=Frame(root)
addFrame=Frame(root)

entry_1=Entry(topFrame)
entry_2=Entry(topFrame,show='*')

entry_1u=Entry(updateFrame)


entry_1d=Entry(deleteFrame)

entry_1add=Entry(addFrame)



###########################################################################
#send mail function  (add button GUI) 
def add_button(): #admin access -> inside admin frame->inside add frame-> add button   
        sendmail.m_send(entry_1add.get())
        tkinter.messagebox.showinfo("Process Complete","Mail Sent")
        entry_1add.delete(0, END)
        

# refresh db/train data (update button GUI)
def update_button(): #admin access ->inside admin frame
        kfe,kfn=load_train_data('train_dump.json')
        scan_faces(kfe, kfn,int(entry_1u.get()))
        tkinter.messagebox.showinfo("Process Complete","Attendance Duration :"+entry_1u.get()+" mins")
        entry_1u.delete(0, END)
        
#delete picture function (delete button GUI)
def delete_button(): #admin access ->inside admin frame 
        flag=0
        if flag==0:
                try:
                        os.remove("pro_face_recog/data/"+entry_1d.get()+".jpg")
                        entry_1d.delete(0, END)
                        tkinter.messagebox.showinfo("Details Updated","User Removed Successfully")
                        flag=1
                except:
                        print("no jpg found")
                        pass
        if flag==0:
                try:
                        os.remove("pro_face_recog/data/"+entry_1d.get()+".png")
                        entry_1d.delete(0, END)
                        tkinter.messagebox.showinfo("Details Updated","User Removed Successfully")
                        flag=1
                except:
                        print("no png found")
                        pass
        if flag==0:
                try:
                        os.remove("pro_face_recog/data/"+entry_1d.get()+".heic")
                        entry_1d.delete(0, END)
                        tkinter.messagebox.showinfo("Details Updated","User Removed Successfully")
                        flag=1
                except:
                        print("no heic found")
                        pass
        if flag==0:
                tkinter.messagebox.showinfo("Error","User not found")
        
        
###############################################################################

#admin login function () 
#shows admin frame
def show_access(): 
        if (empinfo.login(entry_1.get(),entry_2.get()))==True:
        #if entry_1.get()=='a' and entry_2.get()=='a':#for testing purpose
            adminFrame.grid(row=1,column=0)
            entry_2.delete(0, END)
        else :
            tkinter.messagebox.showinfo("Invalid ID or Password","Please enter a valid Admin ID and Password")
            entry_2.delete(0, END)

# INSIDE ADMIN ACCESS GUI FUNCTIONS
# after admin access -> show add/update/delete frame
def show_add():
        if 1==1:
            addFrame.grid(row=2,column=0)           
            
def show_update():
        if 1==1:
            updateFrame.grid(row=3,column=0)
            
def show_delete():
        if 1==1:
            deleteFrame.grid(row=4,column=0)

def refresh_db():
        
        tkinter.messagebox.showinfo("Database Refresh Process","Wait for Process to complete")
        # train function 
        train('train_dump.json')
        tkinter.messagebox.showinfo("Database Refresh Process","New users added successfully!")
      
#admin button - main GUI 
def open_admin():       
    
        
        label_1=Label(topFrame,text="Admin ID")
        label_2=Label(topFrame,text="Password")

        

        label_1.grid(row=3,sticky=E)#use north south N S with sticky
        label_2.grid(row=4,sticky=E)

        entry_1.grid(row=3,column=1)
        entry_2.grid(row=4,column=1)
        
        button_submit=Button(topFrame, text="Submit",fg='green',command=show_access)
        button_submit.grid(row=5,column=1)
        
        button_signup=Button(topFrame, text="Signup",fg='green',command=show_signup)
        button_signup.grid(row=6,column=1)

        
#start attendance / face scanning function (default 10 mins)
def open_emp():
        #loading trained data
        kfe,kfn=load_train_data('train_dump.json')
        #face recognition
        scan_faces(kfe, kfn)
        tkinter.messagebox.showinfo("Process Complete","FASYS Attendance Stopped")
        pass
    
def show_signup():
    #opens admin.py    
    import admin
        
""" FIRST PAGE """    
root.title(':-: FASYS :-: by Anuj Sharma')

top_label=Label(topFrame,text="Please select a category :")
top_label.grid(row=0,columnspan=2)
top_label.config(bg='grey', fg='white')

Admin=Button(topFrame,text='Admin', fg='blue',command=open_admin)
Admin.grid(row=1,column=0,rowspan=1,columnspan=1)
Employee=Button(topFrame,text='Start Attendance', fg='blue',command=open_emp)
Employee.grid(row=1,column=1,rowspan=1,columnspan=1)

photo=PhotoImage(file="admin.png")
label=Label(topFrame,image=photo)
label.grid(row=0,column=2,rowspan=10)



''' admin frame'''

def open_update():
        import update
    
def open_delete():
        import delete

access_a=Label(adminFrame,text="Admin Access Granted")
access_a.grid(row=0,columnspan=2)
access_a.config(bg='grey', fg='red')

add=Button(adminFrame,text='Send Mail', fg='black',command=show_add)
add.grid(row=3,column=0,rowspan=1,columnspan=1)


upd=Button(adminFrame,text='Update Duration', fg='black',command=show_update)
upd.grid(row=2,column=0,rowspan=1,columnspan=1)

dele=Button(adminFrame,text='Remove User', fg='red',command=show_delete)
dele.grid(row=4,column=0,rowspan=1,columnspan=1)

refreshdb=Button(adminFrame,text='Refresh Database', fg='green',command=refresh_db)
refreshdb.grid(row=1,column=0,rowspan=1,columnspan=1)




''' update-> update time duration'''
access_u=Label(updateFrame,text="Start Attendance for Duration")
access_u.grid(row=0,columnspan=2)
access_u.config(bg='grey', fg='white')        


label_1u=Label(updateFrame,text="Enter Duration(mins)")
#label_2u=Label(updateFrame,text="Employee Name")

        

label_1u.grid(row=3,sticky=E)#use north south N S with sticky
#label_2u.grid(row=4,sticky=E)
#due to some reason entry upr declare krni pdi 
entry_1u.grid(row=3,column=1)
#entry_2u.grid(row=4,column=1)
        
button_submitu=Button(updateFrame, text="Start Attendance",fg='blue',command=update_button)
button_submitu.grid(row=5,column=1)

''' add-> email send now'''
access_add=Label(addFrame,text="Enter complete email address")
access_add.grid(row=0,columnspan=2)
access_add.config(bg='grey', fg='white')        


label_1add=Label(addFrame,text="Email address")
#label_2add=Label(addFrame,text="Employee Name")

        

label_1add.grid(row=3,sticky=E)#use north south N S with sticky
#label_2add.grid(row=4,sticky=E)

entry_1add.grid(row=3,column=1)
#entry_2add.grid(row=4,column=1)


        
button_submitadd=Button(addFrame, text="Send Mail",fg='green',command=add_button)
button_submitadd.grid(row=5,column=1)

'''delete'''
access_d=Label(deleteFrame,text="Enter Details for Removing User")
access_d.grid(row=0,columnspan=2)
access_d.config(bg='grey', fg='white')        


label_1d=Label(deleteFrame,text="User ID")

label_1d.grid(row=3,sticky=E)#use north south N S with sticky


entry_1d.grid(row=3,column=1)
        
button_submitu=Button(deleteFrame, text="Remove User",fg='green',command=delete_button)
button_submitu.grid(row=5,column=1)

"""end"""


root.mainloop()

