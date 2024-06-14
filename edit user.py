import tkinter as tk
import MySQLdb

class UserEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("User Editor")

        self.label_id = tk.Label(root, text="User ID:")
        self.label_id.pack()
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

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

        self.button_load = tk.Button(root, text="Load User", command=self.load_user)
        self.button_load.pack()

        self.button_update = tk.Button(root, text="Update User", command=self.update_user)
        self.button_update.pack()

    def load_user(self):
        db = MySQLdb.connect(host='localhost', user='root', password='toor', db='users')
        cur = db.cursor()

        user_id = self.entry_id.get()

        query = "SELECT name, email, password FROM users WHERE id = %s"
        cur.execute(query, (user_id,))
        user = cur.fetchone()

        if user:
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

            self.entry_name.insert(tk.END, user[0])
            self.entry_email.insert(tk.END, user[1])
            self.entry_password.insert(tk.END, user[2])
        else:
            print("User not found!")

        cur.close()
        db.close()

    def update_user(self):
        db = MySQLdb.connect(host='localhost', user='root', password='toor', db='users')
        cur = db.cursor()

        user_id = self.entry_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        query = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"
        values = (name, email, password, user_id)

        cur.execute(query, values)
        db.commit()

        cur.close()
        db.close()

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        print("User updated successfully!")

root = tk.Tk()
app = UserEditor(root)
root.mainloop()