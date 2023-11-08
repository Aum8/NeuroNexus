import tkinter as tk
import random
import string

def generate_password(length):
    if length < 8:
        return "Password length must be at least 8 characters."

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    special_char = random.choice(string.punctuation)
    digit = random.choice(string.digits)

    remaining_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(remaining_characters) for _ in range(length - 4))

    password = lowercase + uppercase + special_char + digit + password

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def generate_password_button():
    try:
        password_length = int(length_entry.get())
        password = generate_password(password_length)
        password_output.config(text="Generated Password: " + password)
    except ValueError:
        password_output.config(text="Invalid input. Please enter a valid number for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password_button)
generate_button.pack()

# Label to display the generated password
password_output = tk.Label(root, text="")
password_output.pack()

# Run the application
root.mainloop()
