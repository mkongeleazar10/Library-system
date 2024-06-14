import tkinter as tk
import MySQLdb

class UserRegistration:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")

        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.button_register = tk.Button(root, text="Register", command=self.register_user)
        self.button_register.pack()

    def register_user(self):
        db = MySQLdb.connect(host='localhost', user='root', password='toor', db='users')
        cur = db.cursor()

        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)

        cur.execute(query, values)
        db.commit()

        cur.close()
        db.close()

        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        print("User registered successfully!")

root = tk.Tk()
app = UserRegistration(root)
root.mainloop()