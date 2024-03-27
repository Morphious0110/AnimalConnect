import tkinter as tk

def add_card():
    name = name_entry.get()
    photo = photo_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()

    # Create a new card frame
    card_frame = tk.Frame(cards_frame, bg="white", bd=2, relief=tk.RIDGE)
    card_frame.pack(padx=5, pady=5)

    # Display information in the card
    tk.Label(card_frame, text="Name: " + name, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Photo: " + photo, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Address: " + address, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Phone: " + phone, bg="white").pack(anchor=tk.W)

def switch_to_card_page():
    input_frame.pack_forget()
    main_menu_frame.pack_forget()
    cards_frame.pack(fill=tk.BOTH, expand=True)

def switch_to_main_menu():
    input_frame.pack(fill=tk.BOTH, expand=True)
    cards_frame.pack_forget()
    main_menu_frame.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Card Grid")

# Main menu frame
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(main_menu_frame, text="Welcome to Card Grid", font=("Helvetica", 18)).pack(pady=20)
tk.Button(main_menu_frame, text="Go to Card Page", command=switch_to_card_page).pack()

# Create input fields
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Photo:").grid(row=1, column=0, sticky=tk.W)
photo_entry = tk.Entry(input_frame)
photo_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Address:").grid(row=2, column=0, sticky=tk.W)
address_entry = tk.Entry(input_frame)
address_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Phone:").grid(row=3, column=0, sticky=tk.W)
phone_entry = tk.Entry(input_frame)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

# Button to add card
add_button = tk.Button(input_frame, text="Add Card", command=add_card)
add_button.grid(row=4, columnspan=2, pady=10)

# Frame to hold cards
cards_frame = tk.Frame(root)

# Button to go back to main menu
back_button = tk.Button(cards_frame, text="Back to Main Menu", command=switch_to_main_menu)
back_button.pack(pady=10)

root.mainloop()
