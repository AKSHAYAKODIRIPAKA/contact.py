import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.pack(pady=10)

        # Entry fields for contact information
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Phone Number:").pack()
        self.phone_entry = tk.Entry(root, width=50)
        self.phone_entry.pack(pady=5)

        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(pady=5)

        # Buttons
        self.add_contact_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT, padx=5)

        self.remove_contact_button = tk.Button(root, text="Remove Contact", command=self.remove_contact)
        self.remove_contact_button.pack(side=tk.LEFT, padx=5)

        self.clear_all_button = tk.Button(root, text="Clear All", command=self.clear_all)
        self.clear_all_button.pack(side=tk.LEFT, padx=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showwarning("Warning", "All fields must be filled out.")
            return

        contact = f"Name: {name}, Phone: {phone}, Email: {email}"
        self.contact_listbox.insert(tk.END, contact)
        
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def remove_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            self.contact_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to remove.")

    def clear_all(self):
        self.contact_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
