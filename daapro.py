import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task_name = task_name_entry.get()
    deadline = deadline_entry.get()
    priority = priority_entry.get()

    if not task_name or not deadline or not priority:
        messagebox.showerror("Input Error", "All fields are required.")
        return
    if priority!=0 or priority!=1:
        messagebox.showerror("Input Error", "Input Valid priority")
        return
    
    task_status = False
    try:
        # Validate the deadline format
        datetime.strptime(deadline, "%Y-%m-%d")
        task = [task_name, deadline, priority, task_status]
        tasks.append(task)
        messagebox.showinfo("Success", "Task added successfully!")
        display_tasks()
    except ValueError:
        messagebox.showerror("Date Error", "Deadline must be in YYYY-MM-DD format.")

# Function to display tasks
def display_tasks():
    tasks_list.delete(0, tk.END)
    if not tasks:
        tasks_list.insert(tk.END, "No tasks found.")
    else:
        for i, task in enumerate(tasks):
            task_info = f"{i+1}. Task: {task[0]}, Deadline: {task[1]}, Priority: {task[2]}, Completed: {'✔' if task[3] else '✖'}"
            tasks_list.insert(tk.END, task_info)

# Function to sort tasks by deadline
def sort_by_deadline():
    tasks.sort(key=lambda x: x[1])
    display_tasks()

# Function to sort tasks by priority
def sort_by_priority():
    tasks.sort(key=lambda x: x[2])
    display_tasks()

# Function to complete a task
def complete_task():

    index = int(task_index_entry.get()) - 1
    if 0 <= index < len(tasks):
        tasks[index][3] = True
        messagebox.showinfo("Success", "Task marked as completed.")
        display_tasks()
    else:
        messagebox.showerror("Error", "Invalid task index.")


# Function to delete a task
def delete_task():

    index = int(task_index_entry.get()) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        messagebox.showinfo("Success", "Task deleted.")
        display_tasks()
    else:
        messagebox.showerror("Error", "Invalid task index.")
    

# Tkinter setup
root = tk.Tk()
root.title("To-Do List Application")

root.configure(bg='lightpink')
# Task Entry
task_name_label = tk.Label(root, text="Task Name:",bg='lightpink')
task_name_label.grid(row=0, column=0, padx=5, pady=5)
task_name_entry = tk.Entry(root)
task_name_entry.grid(row=0, column=1, padx=5, pady=5)

deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD):", bg='lightpink')
deadline_label.grid(row=1, column=0, padx=5, pady=5)
deadline_entry = tk.Entry(root)
deadline_entry.grid(row=1, column=1, padx=5, pady=5)

priority_label = tk.Label(root, text="Priority (1=High, 2=Low):", bg='lightpink')
priority_label.grid(row=2, column=0, padx=5, pady=5)
priority_entry = tk.Entry(root)
priority_entry.grid(row=2, column=1, padx=5, pady=5)

add_task_button = tk.Button(root, text="Add Task", command=add_task, bg='blue', fg='white')
add_task_button.grid(row=3, column=1, pady=10)

# Task Display
tasks_list = tk.Listbox(root, width=80, height=10)
tasks_list.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Sorting buttons
sort_deadline_button = tk.Button(root, text="Sort by Deadline", command=sort_by_deadline, bg='navy', fg='white')
sort_deadline_button.grid(row=5, column=0, padx=5, pady=5)

sort_priority_button = tk.Button(root, text="Sort by Priority", command=sort_by_priority, bg='navy', fg='white')
sort_priority_button.grid(row=5, column=1, padx=5, pady=5)

# Update and delete task
task_index_label = tk.Label(root, text="Task Index:", bg='lightpink')
task_index_label.grid(row=6, column=0, padx=5, pady=5)
task_index_entry = tk.Entry(root)
task_index_entry.grid(row=6, column=1, padx=5, pady=5)

complete_task_button = tk.Button(root, text="Complete Task", command=complete_task, bg='purple', fg='white')
complete_task_button.grid(row=7, column=0, padx=5, pady=5)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, bg='maroon', fg='white')
delete_task_button.grid(row=7, column=1, padx=5, pady=5)

# Display initial tasks
display_tasks()

# Start the Tkinter loop
root.mainloop()
