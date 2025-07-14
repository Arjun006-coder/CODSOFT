import json
import os
import tkinter as tk
from tkinter import messagebox

DATA_FILE = "contacts.json"

class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_contacts(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, number, address, email):
        self.contacts[name] = {
            "number": number,
            "address": address,
            "email": email
        }
        self.save_contacts()

    def update_contact(self, name, number, address, email):
        if name in self.contacts:
            self.contacts[name] = {
                "number": number,
                "address": address,
                "email": email
            }
            self.save_contacts()
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return True
        return False

    def search_contact(self, name):
        return self.contacts.get(name, None)

    def get_all_contacts(self):
        return self.contacts


# --------------------- GUI --------------------- #

book = ContactBook()

def add_contact():
    def save():
        name_val = name.get()
        if not name_val:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        book.add_contact(name_val, number.get(), address.get(), email.get())
        messagebox.showinfo("Success", "Contact added successfully.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Add Contact")
    labels = ["Name", "Phone Number", "Address", "Email"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label).grid(row=i, column=0)
        entry = tk.Entry(win, width=30)
        entry.grid(row=i, column=1)
        entries.append(entry)

    name, number, address, email = entries
    tk.Button(win, text="Save Contact", command=save).grid(row=4, columnspan=2, pady=10)

def update_contact():
    def save():
        if book.update_contact(name.get(), number.get(), address.get(), email.get()):
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Update Contact")
    labels = ["Name", "New Phone", "New Address", "New Email"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(win, text=label).grid(row=i, column=0)
        entry = tk.Entry(win, width=30)
        entry.grid(row=i, column=1)
        entries.append(entry)

    name, number, address, email = entries
    tk.Button(win, text="Update Contact", command=save).grid(row=4, columnspan=2, pady=10)

def search_contact():
    def search():
        contact = book.search_contact(name.get())
        if contact:
            result.set(f"Number: {contact['number']}\nAddress: {contact['address']}\nEmail: {contact['email']}")
        else:
            result.set("Contact not found.")

    win = tk.Toplevel(root)
    win.title("Search Contact")
    tk.Label(win, text="Enter Name:").grid(row=0, column=0)
    name = tk.Entry(win, width=30)
    name.grid(row=0, column=1)
    result = tk.StringVar()
    tk.Button(win, text="Search", command=search).grid(row=1, columnspan=2, pady=5)
    tk.Label(win, textvariable=result, justify="left", fg="blue").grid(row=2, columnspan=2)

def delete_contact():
    def delete():
        if book.delete_contact(name.get()):
            messagebox.showinfo("Deleted", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        win.destroy()

    win = tk.Toplevel(root)
    win.title("Delete Contact")
    tk.Label(win, text="Enter Name:").grid(row=0, column=0)
    name = tk.Entry(win, width=30)
    name.grid(row=0, column=1)
    tk.Button(win, text="Delete", command=delete).grid(row=1, columnspan=2, pady=5)

def view_contacts():
    win = tk.Toplevel(root)
    win.title("Contact List")
    contacts = book.get_all_contacts()
    if not contacts:
        tk.Label(win, text="No contacts to display.").pack()
        return

    for name, info in contacts.items():
        text = f"{name} - {info['number']}, {info['address']}, {info['email']}"
        tk.Label(win, text=text, anchor="w", justify="left").pack(anchor="w", padx=10, pady=2)

# ------------------- Main Window ------------------- #

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x300")

tk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Button(root, text="Add Contact", width=25, command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=25, command=update_contact).pack(pady=5)
tk.Button(root, text="Search Contact", width=25, command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=25, command=delete_contact).pack(pady=5)
tk.Button(root, text="View Contact List", width=25, command=view_contacts).pack(pady=5)

root.mainloop()
