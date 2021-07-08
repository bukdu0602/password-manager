import tkinter.messagebox
from tkinter import *
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def passwordgenerating():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    list_comp1 = [random.choice(letters) for num in range(nr_letters)]

    list_comp2 = [random.choice(symbols) for num2 in range(nr_symbols)]

    list_comp3 = [random.choice(numbers) for num3 in range(nr_numbers)]

    password_list = list_comp1 + list_comp2 + list_comp3


    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    return password

def password_generator():
    password_input.delete(0, END)
    newpass = passwordgenerating()
    password_input.insert(END, newpass)
    pyperclip.copy(newpass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = Email_username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword:{password}\nIs it ok to save?")

        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website} | {email_username} | {password}\n")
            file.close()
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
filename = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=filename)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

Email_username = Label(text="Email/Username: ")
Email_username.grid(row=2, column=0)

Email_username_input = Entry(width=35)
Email_username_input.insert(END, 'ryan.hyun@gmail.com')
Email_username_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ")
password.grid(row=3, column=0)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", command=password_generator)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()