import tkinter as tk
from tkinter import ttk

def insert_data():
    data = entry.get()
    tree.insert("", "end", values=(len(tree.get_children()) + 1, data))
    entry.delete(0, 'end')

app = tk.Tk()
app.title("Serial Number in Treeview")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

tree = ttk.Treeview(frame, columns=("Serial Number", "Data"), show="headings")
tree.heading("Serial Number", text="Serial Number")
tree.heading("Data", text="Data")
tree.pack()

entry = ttk.Entry(frame)
entry.pack()

add_button = ttk.Button(frame, text="Add Data", command=insert_data)
add_button.pack()

app.mainloop()
