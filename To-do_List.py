import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)
task_entry.focus_set()

# Add Button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task List
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
task_list.pack()

# Delete Button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the application
root.mainloop()
