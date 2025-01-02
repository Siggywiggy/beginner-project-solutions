#! python3
# a program that allows user input as desired time and gives a countdown from current time


from datetime import datetime
import pyinputplus as pyip
import time
import sys

user_input = pyip.inputDatetime(
    prompt="Enter date and time Day/Month/Year Hours:Minutes \n ",
    formats=(
        "%d/%m/%y %H:%M",
        "%d/%m/%Y %H:%M",
        "%-d/%m/%y %H:%M",
        "%-d/%m/%Y %H:%M",
        "%d/%-m/%y %H:%M",
        "%d/%-m/%Y %H:%M",
        "%-d/%-m/%y %H:%M",
        "%-d/%-m/%Y %H:%M",
        "%d/%B/%y %H:%M",
        "%d/%B/%Y %H:%M",
        "%-d/%B/%y %H:%M",
        "%-d/%B/%Y %H:%M",
    ),
)

while True:
    current_time = datetime.now()
    time_left = user_input - current_time

    if user_input < current_time:
        print("your desired time in in the past, try again!")
        continue

    print(f"{str(time_left).split('.')[0]} left until {user_input}...")
    time.sleep(1)

    if time_left.seconds <= 1:
        print("Countdown has finalized!")
        break
