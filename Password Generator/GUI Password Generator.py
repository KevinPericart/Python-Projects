import tkinter as tk
import string
import random
def random_password() :
    password = []
    for i in range(4):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        passwords = " ".join(str(x)for x in password)
        label.config(text = passwords)
app = tk.Tk()
app.geometry("400x100")
button = tk.Button(app, text = "Generate Password", command = random_password)
button.grid(row = 1, column = 1)
label = tk.Label(app, font = ("arial", 13, "bold"))
label.grid(row = 9, column = 3)
app.mainloop()
