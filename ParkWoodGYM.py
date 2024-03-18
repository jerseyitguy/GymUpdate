from tkinter import *
from tkinter import messagebox
import os




def MainMenu():

        
    MainMenuWin=Tk()
    MainMenuWin.title("Main Menu")
    MainMenuWin.geometry("200x200")
    
    frame1=Frame(MainMenuWin)
    frame1.pack()
                           
    btn1=Button(frame1,text="Add Staff",command=AddStaff)
    btn2=Button(frame1,text="Payroll",command= Payroll)
    
    frame2=Frame(MainMenuWin)
    frame2.pack()

    btn3=Button(frame2,text="Add User",command=AddUser)
    
    frame3=Frame(MainMenuWin)
    frame3.pack()

    btn4=Button(frame3,text="Logout",command=LoginScreen)
    btn5=Button(frame3,text="Exit",command=MainMenuWin.destroy)
            
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)
            
def Payroll():
    
    os.system('python Payroll.py')
    
def AddStaff():

    def SaveStaff() :

        StaffIDSave = StaffIDVar.get()
        StaffIDSave = StaffIDSave.ljust(50)
    
        FirstnameSave = FirstnameVar.get()
        FirstnameSave = FirstnameSave.ljust(50)
    
        SurnameSave = SurnameVar.get()
        SurnameSave = SurnameSave.ljust(50)
    
        AddressSave = AddressVar.get()
        AddressSave = AddressSave.ljust(50)
    
        PostCodeSave = PostCodeVar.get()
        PostCodeSave = PostCodeSave.ljust(50)

      
    
        fileObject = open("StaffDetails.txt","a")
        
        fileObject.write(StaffIDSave + FirstnameSave + SurnameSave + AddressSave + PostCodeSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Staff details successfully saved")
    
    AddStaffWin=Tk()
    AddStaffWin.title("Add Staff")
    AddStaffWin.geometry("300x300")
    
    frame1=Frame(AddStaffWin)
    frame1.pack()

       
    Label(frame1, text="StaffID").grid(row=3, column=0, sticky=W)
    StaffIDVar=StringVar()
    StaffIDVar= Entry(frame1, textvariable=StaffIDVar)
    StaffIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Firstname").grid(row=4, column=0, sticky=W)
    FirstnameVar=StringVar()
    FirstnameVar= Entry(frame1, textvariable=FirstnameVar)
    FirstnameVar.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Surname").grid(row=5, column=0, sticky=W)
    SurnameVar=StringVar()
    SurnameVar= Entry(frame1, textvariable=SurnameVar)
    SurnameVar.grid(row=5,column=1,sticky=W)
    
    Label(frame1, text="Address").grid(row=6, column=0, sticky=W)
    AddressVar=StringVar()
    AddressVar= Entry(frame1, textvariable=AddressVar)
    AddressVar.grid(row=6,column=1,sticky=W)
    
    Label(frame1, text="Postcode").grid(row=7, column=0, sticky=W)
    PostCodeVar=StringVar()
    PostCodeVar= Entry(frame1, textvariable=PostCodeVar)
    PostCodeVar.grid(row=7,column=1,sticky=W)

  

    frame2 = Frame(AddStaffWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddStaffWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveStaff)
    b1.pack(side=LEFT); b2.pack(side=LEFT)



    
    

    
def AddUser():
    
    def SaveUser() :

        UserIDSave = UserIDVar.get()
        UserIDSave = UserIDSave.strip()
    
        PasswordSave = PasswordVar.get()
        PasswordSave = PasswordSave.strip()
    
       
        fileObject = open("data.dat","a")
        
        fileObject.write(UserIDSave + " " + PasswordSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Password successfully saved")
    
    AddUserWin=Tk()
    AddUserWin.title("Add User")
    AddUserWin.geometry("300x300")
    
    frame1=Frame(AddUserWin)
    frame1.pack()

       
    Label(frame1, text="UserID").grid(row=3, column=0, sticky=W)
    UserIDVar=StringVar()
    UserIDVar= Entry(frame1, textvariable=UserIDVar)
    UserIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Password").grid(row=4, column=0, sticky=W)
    PasswordVar=StringVar()
    PasswordVar= Entry(frame1, textvariable=PasswordVar)
    PasswordVar.grid(row=4,column=1,sticky=W)
    
     

    frame2 = Frame(AddUserWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddUserWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveUser)
    b1.pack(side=LEFT); b2.pack(side=LEFT)

    
    
def LoginScreen():
    
    def login():
        username=usname.get()
        passwd=password.get()
        flag=TRUE#3)b)this value can only have two values - true or false- and is used when ensuring the password/username is correct

        if username.strip() == "" and passwd.strip() == "":#3)c) the line of code undernetah this one will only run if the user has left the username and password blank
            messagebox.showinfo("Error","Blank username and password")
        elif passwd.strip() == "":
            messagebox.showinfo("Error","Blank password")
        elif username.strip()== "":
            messagebox.showinfo("Error","Blank username")
        else:
            
            passwordfile = open("data.dat","r")
            passvar = passwordfile.readline()
                            
            while flag and passvar !="":#3)a)the part of indented code underneath this line will repeat until the correct username and password is used
                                      
                if passvar.find(username.strip()) >=0 and passvar.find(passwd.strip())>=0:
                    messagebox.showinfo("Authenticated","Correct username and password")
                    flag = FALSE
                                    
                passvar = passwordfile.readline()
                                
                passwordfile.close()
                if flag:
                 messagebox.showinfo("Error","Incorrect username and / or password")
                else:
                    loginwindow.destroy()
                    MainMenu()
                                

        
    loginwindow=Tk()
    loginwindow.title("Log In Screen")
    loginwindow.geometry("200x200")
    lbluname=Label(loginwindow, text="Username")
    usname=Entry(loginwindow)
    lblpass=Label(loginwindow, text="Password")
    password=Entry(loginwindow)

    lbluname.pack()
    usname.pack()
    lblpass.pack()
    password.pack()

    btn=Button(loginwindow,text="Log In",command=login).pack()

    loginwindow.mainloop()



LoginScreen()     
