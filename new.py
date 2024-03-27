from tkinter import *
from PIL import Image, ImageTk
from sidebar import create_sidebar
import lecture_page as lecture_page,Volunteer_page as Volunteer_page,Rescue as Rescue,teacher_section
def open_lecture_page():
    print("Opening Lecture Page...")
   
    lecture_page()

def open_Volunteer_page():
    print("Opening Volunteer Page...")
   
    Volunteer_page()

def open_teacher_section():
    print("Opening Teacher Section Page...")
  
    teacher_section()

def open_Rescue():
    print("Opening Rescue Page...")
    
    Rescue()

root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")


topbar,sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)

root.mainloop()
