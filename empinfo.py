#database connection csv file
import csv
from datetime import datetime
import pandas as pd
import base64



#create new admin
def signup(user_name,passwrd):
    encodp=base64.b64encode(bytes(passwrd, 'utf-8'))
    with open('Admin.csv',mode='a') as f1:
        pass
    users=[]
    try:
        
        d=pd.read_csv("Admin.csv",header=None)#-1
        users=d.iloc[:,0].tolist()
    except pd.errors.EmptyDataError:
        pass
        
    
    if user_name in users:
        print("already acount")
        return False
    else:
        with open('Admin.csv', mode='a',newline='') as file:
            writer= csv.writer(file)
    
            #way to write to csv file
            writer.writerows([[user_name,encodp]])
            print("account created")
            return True

      
#admin login check
def login(user_name,passwrd):
    encodp=base64.b64encode(bytes(passwrd, 'utf-8'))
    with open('Admin.csv','r')as f:
        data = csv.reader(f)
        for row in data:
            try:
                if user_name==row[0]:
                    if str(encodp)==str(row[1]):
                        print("login sucessfull")
                        return True
                    else:
                        print("wrong password")
                        return False
            except:
                print("error")
                return False



