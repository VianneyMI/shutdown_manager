from timestamp import Timestamp
from functions import *
import time

# Init Window
root = tk.Tk()
timestamp=Timestamp(date=datetime.date.today(),time=datetime.datetime.now().strftime("%H:%M"))
ttk.Button(root, text='Select Date', command=lambda: select_date(root,timestamp)).pack(padx=15, pady=10)
ttk.Button(root, text='Select Time', command=lambda: select_time(root,timestamp)).pack(padx=15, pady=10)
root.mainloop()
print(timestamp.date)
print(timestamp.time)
print(timestamp.to_seconds()-datetime.datetime.now().timestamp())
