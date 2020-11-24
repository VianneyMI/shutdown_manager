import os
# Use a web app to display the calendar and get the timestamp and return it to Python
delay=int(input('In how many seconds do you want to shudwon your computer ?'))
command="shutdown /s /t " + str(delay)
os.system(command)