from tkinter import *
from PIL import Image, ImageTk
from sidebar import create_sidebar
import lecture_page as lecture_page, adoption_page as adoption_page, Rescue as Rescue, adoption_page
import subprocess
import tkinter as tk

def open_lecture_page():
    root.destroy()
    subprocess.run(["python", "lecture_page.py"])

def open_adoption_page():
    root.destroy()
    subprocess.run(["python", "adoption_page.py"])

def open_teacher_section():   
    root.destroy()
    subprocess.run(["python", "adoption_page.py"])

def open_Rescue():
    root.destroy()

root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")

# Create topbar, sidebar, and buttons
topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_adoption_page, open_teacher_section, open_Rescue)

# Add a label for welcome message
welcome_label = Label(root, text="Welcome to Animal Connect", font=("Arial", 20))
welcome_label.pack(pady=20)  # Adjust pady value as needed to position the label

root.mainloop()
