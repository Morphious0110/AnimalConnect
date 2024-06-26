from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
# from mini-project-main import new


#Functionality Part
def on_usernameEnter(event):
    if usernameEntry.get()=="Username":
        usernameEntry.delete(0,END)
def on_passwordEnter(event):
    if passwordEntry.get()=="Password":
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def open_signupPage():
    login_window.destroy()
    import signup

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Add your authentication logic here
    # For simplicity, let's check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # open_option_panel(root)
        login_window.destroy()
        import new
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


#GUI part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)

bgImage = ImageTk.PhotoImage(file='images/1.jpg')
# bgImage = Tk.PhotoImage(file="1.png")
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold underline'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#username Entry
usernameEntry = Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,"Username")
usernameEntry.bind('<FocusIn>', on_usernameEnter)

Frame(login_window,height=2,width=250,bg='firebrick1').place(x=580,y=222)

#Password Entry
passwordEntry = Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,"Password")
passwordEntry.bind('<FocusIn>', on_passwordEnter)

Frame(login_window,height=2,width=250,bg='firebrick1').place(x=580,y=282)

openeye = PhotoImage(file='images/openeye.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton = Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',fg='firebrick1',font=('Microsoft Yahei UI Light',9,'bold'))
forgetButton.place(x=715,y=295)

loginButton = Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',cursor='hand2',bd=0,width=19,foreground='white',command=login)
loginButton.place(x=578,y=350)

orLabel = Label(login_window,text='--------------OR--------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='images/facebook.png')
fbLabel = Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='images/google.png')
gogLabel = Label(login_window,image=google_logo,bg='white')
gogLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='images/twitter.png')
twitterLabel = Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signUpLabel = Label(login_window,text='Dont Have An Account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signUpLabel.place(x=590,y=500)

newaccountButton = Button(login_window,text='Create new one!',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',cursor='hand2',bd=0,foreground='blue',command=open_signupPage)
newaccountButton.place(x=727,y=500)


login_window.mainloop()