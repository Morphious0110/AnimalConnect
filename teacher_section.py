from tkinter import *
import tkinter as tk
from sidebar import create_sidebar  # Import the create_sidebar function
import subprocess
def open_lecture_page():
    print("Opening Lecture Page...") 
    root.destroy()

    subprocess.run(["python", "lecture_page.py"])
def open_Volunteer_page():
    print("Opening Volunteer Page...")
    root.destroy()

    subprocess.run(["python", "Volunteer_page.py"])
def open_teacher_section():
    print("Opening Teacher Section Page...")
    root.destroy()

    subprocess.run(["python", "teacher_section.py"])
def open_Rescue():
    print("Opening Rescue Page...")
    root.destroy()

    subprocess.run(["python", "Rescue.py"])

root = Tk()
root.title("Volunteer Page")

root.title("Animal Connect")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page,open_lecture_page,open_Rescue,open_teacher_section)

# Create a frame for the buttons in the white portion
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Add the two additional buttons in the middle
# add_campaign_button = Button(button_frame, text="Adopt a pet", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))  # Adjust pady to add space
# view_campaign_button = Button(button_frame, text="post pet for adoption", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))  # Adjust pady to add space
label = tk.Label(root, text="Adoption")

# Pack the label widget to display it in the window
label.pack()
# Insert a space between the existing buttons and the new ones

Label(button_frame, text="").pack(side=TOP, pady=10)
   
# Configure button commands
for button in buttons:
    button.config(command=open_Volunteer_page)

root.mainloop()
