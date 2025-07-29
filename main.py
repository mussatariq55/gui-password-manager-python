from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Character sets for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random characters from each set
    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    # Combine all and shuffle
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    # Join and display the password
    password = "".join(password_list)
    pyperclip.copy(password)  # Automatically copies to clipboard
    password_input.insert(index=0, string=password)


# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    to_search = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[to_search.title()]["email"]
            password = data[to_search.title()]["password"]
    except:
        # If file not found or website doesn't exist
        messagebox.showinfo(title="Error", message=f"No details for the {to_search} found.")
    else:
        # Show email and password in a popup
        messagebox.showinfo(title=f"{to_search}", message=f"Website: {to_search}\nEmail: {email}\nPassword: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # Prepare the data structure
    new_data = {
        website: {
            "email": email.lower(),
            "password": password
        }
    }

    # Check if any field is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left any fields empty.")
    else:
        # Ask for confirmation before saving
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"Website: {website}\nEmail: {email}\nPassword: {password}\nDo you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump({}, file)
            else:
                # Update the existing data
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                # Clear the entry fields
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# App logo
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Entry fields
website_input = Entry(width=32)
website_input.grid(row=1, column=1, sticky="W")
website_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2, sticky="W")
email_input.insert(0, "example@email.com")  # Default placeholder

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="W")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2, sticky="W")

# Run the app
window.mainloop()
