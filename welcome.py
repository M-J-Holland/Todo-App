import datetime


def welcome_messages():
    welcome_message = "Welcome to the Python CLI TODO App"
    now = datetime.datetime.now()
    date_time = now.strftime("%A %d %B %Y, %H:%M:%S")
    date, time = date_time.split(", ")
    print(welcome_message)
    print(f"It is: {date}\nAnd the time is: {time}")