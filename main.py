from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Generate Password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range (randint(2, 4))]
    password_list += [choice(numbers) for i in range (randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# Save Passwowrd
def add():
    website = website_entry.get().title()
    user = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if website == "" or user == "" or password == "":
        messagebox.showwarning(title="Empty Fields", message="Don't forget to fill out all fields!")
    else:
        correct = messagebox.askokcancel(title=website, message=f"You entered: \nUsername: {user} "
                               f"\nPassword: {password} \nIs this correct?")
        if correct:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                email_username_entry.delete(0, END)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# Search Function
def search():

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="You do not have a KeyKeep file yet.")

    website = website_entry.get().title()

    if website == "":
        messagebox.showwarning(title="Empty Fields", message="Don't forget to fill out all fields!")

    elif website in data:
        user = data[website]["user"]
        password = data[website]["password"]
        messagebox.showinfo(title=website_entry.get().title(), message=f"User: {user}\nPassword: {password}")
    else:
        messagebox.showwarning(title="Website Not Found", message=f"{website} is not in your KeyKeep file.")



# UI Setup
window = Tk()
window.title("KeyKeep")
window.config(padx=100, pady=20)

canvas = Canvas(width=270, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 0, anchor="n", image=logo_img)  # Adjust x-coordinate here
canvas.grid(column=1, row=0, columnspan=2, sticky="ew")

website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky="E")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="ew")

email_username_entry = Entry(width=44)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

add_button = Button(text="Add", command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

gen_pw_button = Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3, sticky="ew")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="ew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=0)

window.mainloop()
