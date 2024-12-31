#! python3
# a program that allows user input as desired time and gives a countdown from current time


from datetime import datetime
import pyinputplus as pyip

current_time = datetime.now()

print(f'{current_time} is current time')

user_input = pyip.inputDatetime(prompt='Enter date and time Day/Month/Year Hours:Minutes \n ',
                                formats=('%d/%m/%y %H:%M', '%d/%m/%Y %H:%M', '%-d/%m/%y %H:%M', '%-d/%m/%Y %H:%M',
                                         '%d/%-m/%y %H:%M', '%d/%-m/%Y %H:%M', '%-d/%-m/%y %H:%M',
                                         '%-d/%-m/%Y %H:%M', '%d/%B/%y %H:%M', '%d/%B/%Y %H:%M', '%-d/%B/%y %H:%M',
                                         '%-d/%B/%Y %H:%M'))

print(user_input)

time_left = user_input - current_time

print(time_left)