import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def validate_date(cal,timestamp):
    timestamp.set_date(cal.selection_get())

def select_date(root,timestamp):
    top = tk.Toplevel(root)
    cal = Calendar(top, selectmode='day')
    #date = cal.datetime.today() + cal.timedelta(days=2)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=lambda: validate_date(cal,timestamp)).pack()

def validate_time(hour_picker, minute_picker, timestamp):
    timestamp.set_time(datetime.time(int(hour_picker.get()),int(minute_picker.get())).strftime("%H:%M"))

def select_time(root,timestamp):
    top = tk.Toplevel(root)

    hour_label=tk.Label(top, text="H")
    hour_label.grid(row=0, column=0)

    hour_picker = tk.Spinbox(top, from_=0, to=23)
    hour_picker.grid(row=0, column=1)

    minute_label=tk.Label(top, text="Min")
    minute_label.grid(row=1, column=0)

    minute_picker = tk.Spinbox(top, from_=0, to=59)
    minute_picker.grid(row=1, column=1)

    ttk.Button(top, text="ok", command=lambda: validate_time(hour_picker, minute_picker, timestamp)).grid(row=2,column=1)
