import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eledikoks10",
    database="library"
)
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Download Book")

# Create the book selection dropdown
cursor.execute("SELECT title FROM books")
book_titles = [row[0] for row in cursor.fetchall()]

selected_book = tk.StringVar()
book_dropdown = ttk.Combobox(root, textvariable=selected_book, values=book_titles)
book_dropdown.grid(row=0, column=0, padx=10, pady=10)

# Create the download button
download_button = tk.Button(root, text="Download", command=lambda: download_book())
download_button.grid(row=0, column=1, padx=10, pady=10)

# Define the function to download the book
def download_book():
    selected_title = selected_book.get()
    cursor.execute("SELECT file_data, file_type FROM books WHERE title = %s", (selected_title,))
    book_data, file_type = cursor.fetchone()
    
    # Open a file dialog to select the download location
    download_path = filedialog.asksaveasfilename(
        defaultextension=f".{file_type}",
        filetypes=[(f"{file_type.upper()} Files", f"*.{file_type}")],
        initialfile=f"{selected_title}.{file_type}"
    )
    
    if download_path:
        # Write the book data to the selected file
        with open(download_path, "wb") as file:
            file.write(book_data)
        
        # Display a success message
        tk.messagebox.showinfo("Download Complete", f"The book '{selected_title}' has been downloaded.")

# Run the main loop
root.mainloop()

# Close the database connection
conn.close()