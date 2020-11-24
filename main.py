import time
from functions import *
from timestamp import Timestamp


# Init Window
root = tk.Tk()

now=datetime.datetime.now()
timestamp=Timestamp(date=datetime.date.today(),time=datetime.datetime.now().strftime("%H:%M"))

delay=timestamp.to_seconds()-now.timestamp()

ttk.Button(root, text='Select Date', command=lambda: select_date(root,timestamp)).pack(padx=15, pady=10)
ttk.Button(root, text='Select Time', command=lambda: select_time(root,timestamp)).pack(padx=15, pady=10)
ttk.Button(root, text='ok', command=lambda: validate_datetime(root, delay)).pack()

root.mainloop()
