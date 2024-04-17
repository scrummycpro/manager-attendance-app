import tkinter as tk
from tkinter import ttk
import sqlite3

# Create SQLite database and table if not exists
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY,
                name TEXT,
                attendance_type TEXT,
                points REAL
            )''')
conn.commit()

def submit_attendance():
    name = name_entry.get()
    attendance_type = attendance_var.get()
    points = 0.0

    if attendance_type == "Forced Early out - before two hours":
        points = 1.0
    elif attendance_type == "Forced earlyout After two hours":
        points = 0.5
    elif attendance_type == "Call out":
        points = 1.0
    elif attendance_type == "Call out consecutive":
        points = 0.5
    elif attendance_type == "Late":
        points = 0.5
    elif attendance_type == "No call no show":
        points = 6.0

    # Insert data into the database
    c.execute("INSERT INTO attendance (name, attendance_type, points) VALUES (?, ?, ?)", (name, attendance_type, points))
    conn.commit()

    # Clear entry fields
    name_entry.delete(0, tk.END)

    # Display notification
    notification_label.config(text="Record updated")

root = tk.Tk()
root.title("Attendance Tracker")

# Name entry
name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Attendance type selection
attendance_label = ttk.Label(root, text="Attendance Type:")
attendance_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
attendance_var = tk.StringVar()
attendance_combobox = ttk.Combobox(root, textvariable=attendance_var, values=[
    "Forced Early out - before two hours",
    "Forced earlyout After two hours",
    "Call out",
    "Call out consecutive",
    "Late",
    "No call no show"
])
attendance_combobox.grid(row=1, column=1, padx=5, pady=5)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_attendance)
submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Notification label
notification_label = ttk.Label(root, text="")
notification_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
