from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_generator = "".join(password_list)
    password_input.insert(0, password_generator)
    pyperclip.copy(password_generator)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_name.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=log_img)
canvas.grid(column=2, row=1)

label_1 = Label(text="Website:")
label_1.grid(column=1, row=2)

website_name = Entry(width=40)
website_name.grid(column=2, row=2, columnspan=2)
website_name.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=1)

username_input = Entry(width=40)
username_input.insert(0, "username134@gmail.com")
username_input.grid(row=3, column=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

password_input = Entry(width=21)
password_input.grid(row=4, column=2)

generate_password = Button(text="Generate Password:", command=generate)
generate_password.grid(row=4, column=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
