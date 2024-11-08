#! python3
# simulate a magic 8-ball
import random
import time
import sys



answers = ['Yes', 'No', 'Maybe', 'Defintely not', 'Once in a blue moon', 'More then likely, no', 'More then likely, yes', 'Fifty-fifty chance']

while True:

    print('Please think of a yes/no question or enter q to quit: \n')

    user_input = input()

    if user_input == 'q':
        break
    else:
        answer = random.randint(0, len(answers)-1)
        print('Thinking...')
        time.sleep(2)
        print(answers[answer])

sys.exit()