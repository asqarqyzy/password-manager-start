from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list.extend([choice(SYMBOLS) for _ in range(randint(2, 4))])
    password_list.extend([choice(NUMBERS) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    pass_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if website == "" or password == "":
        messagebox.showerror(title="Error", message=f"Please dont leave any fields empty")
    else:
        try:
        #read-->update
            with open("data.json", "r") as file:
                json_data = json.load(file)
        except FileNotFoundError:
        #create
            with open("data.json", "w") as file:
                json.dump(pass_data, file, indent=4)
        else:
            json_data.update(pass_data)
            # save
            with open("data.json", "w") as file:
                json.dump(json_data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            website_entry.focus()
            pass_entry.delete(0, "end")
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data in dictionary. Pls insert first.")
    else:
        try:
            website_in_data = data[website]
        except KeyError:
            messagebox.showerror(title="Error", message="No password for this website.")
        else:
            messagebox.showinfo(title=website, message=f"Email: {website_in_data["email"]}\n"
                                                       f"Password: {website_in_data["password"]}")
    finally:
        website_entry.delete(0, "end")
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=canvas_img)
canvas.grid(row=0, column=1, columnspan=2)

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

website_entry = Entry(width=22)
search_button = Button(text="Search", width=15, command=find_password)
email_entry = Entry(width=40)
pass_entry = Entry(width=22)
pass_button = Button(text="Generate password", width=15, command=generate)
add_button = Button(text="Add", width=35, command=save)

website_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)
pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

website_entry.focus()
email_entry.insert(0, "nurlybayevaassel@gmail.com")




window.mainloop()