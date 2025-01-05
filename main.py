from tkinter import *
from tkinter import messagebox
import random
import json
FONT = ("Times New Roman",12,"normal")
DEFAULT_EMAIL = "user@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    letter_low = [letter.lower() for letter in letters]
    letters.extend(letter_low)

    # Create a list of numbers and symbol
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

    # main program
    # Create a list of password
    password_letter = [random.choice(letters) for i in range(0, random.randint(8,10))]
    password_symbol = [random.choice(symbol) for i in range(0, random.randint(2,4))]
    password_number = [random.choice(number) for i in range(0, random.randint(2,4))]

    # FINALE PASSWORD
    password_char = []
    password_char.extend(password_letter)
    password_char.extend(password_number)
    password_char.extend(password_symbol)
    random.shuffle(password_char)

    password = "".join(password_char)
    password_entry.delete(0,END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get().title()
    email_name = email_entry.get()
    password_name = password_entry.get()

    user_input = {
        website_name: {
            "email": email_name,
            "password": password_name,
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        if not search(pop_up=False):
            confirm_yes = messagebox.askokcancel(title="Confirmation", message=f"Are you sure you want to save the email and password for {website_name} as {email_name} and {password_name}")
            if confirm_yes:
                try:
                    with open("data.json", "r") as data:
                        data_dic = json.load(data)
                        data_dic.update(user_input)
                except:
                    with open("data.json", "w") as data:
                        json.dump(user_input, data, indent=4)
                else:
                    with open("data.json", "w") as data:
                        json.dump(data_dic, data, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def search(**kwargs):
    error_popped_up = kwargs.get("pop_up")
    searched_data = website_entry.get().title()
    try:
        with open("data.json", "r") as data:
            data_dic = json.load(data)

        email = data_dic[searched_data]["email"]
        password = data_dic[searched_data]["password"]
    except:
        if error_popped_up != False:
            messagebox.showerror(title="Error", message="Data Not Found")
    else:
        if error_popped_up == False:
            messagebox.showerror(title="Error", message="User's already existed!")
        messagebox.showinfo(title=searched_data, message=f"Email: {email} \nPassword: {password}")
        return True




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

logo_png = PhotoImage(file="logo.png")
canva = Canvas(width=200, height=200)
canva.create_image(100,100, image=logo_png)
canva.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=17)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.insert(0, DEFAULT_EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password",command=create_password)
password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Search",command=search, width=10)
search_button.grid(column=2,row=1)









window.mainloop()