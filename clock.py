import time
import os
from datetime import datetime

def countdownTimer(minutes, seconds):
    while minutes or seconds > 0:
        os.system('clear')


        minutes = int(minutes)
        seconds = int(seconds)

        print(str(minutes) + " minutes " + str(seconds) + " seconds left")

        if seconds == 0 and minutes > 0:
            minutes = minutes - 1
            seconds = 59

        else:
            seconds = seconds - 1

        time.sleep(1)

    os.system('clear')
    dateTimeObj = datetime.now()
    for i in range(5):
        print('  _______ _                       _    _                            _          _ ')
        print(' |__   __(_)                     | |  | |                          | |        | |')
        print('    | |   _ _ __ ___   ___ _ __  | |__| | __ _ ___    ___ _ __   __| | ___  __| |')
        print("    | |  | | '_ ` _ \ / _ \ '__| |  __  |/ _` / __|  / _ \ '_ \ / _` |/ _ \/ _` |")
        print('    | |  | | | | | | |  __/ |    | |  | | (_| \__ \ |  __/ | | | (_| |  __/ (_| |')
        print('    |_|  |_|_| |_| |_|\___|_|    |_|  |_|\__,_|___/  \___|_| |_|\__,_|\___|\__,_|')
        print('')
        print('')
        print("    TIMER ENDED AT " + str(dateTimeObj.hour) + ":" + str(dateTimeObj.minute)+ ":" + str(dateTimeObj.second))
        time.sleep(1)
        os.system('clear')
        time.sleep(0.5)


def timer():
    print('How many minutes')
    minutes = input()

    while not minutes.isdigit():
        print('Enter correct number please')
        minutes = input()

    print('how many seconds (leave blank if zero')
    seconds = input()

    if seconds == '':
        seconds = '0'
    while not seconds.isdigit():
        print('Enter correct number please!')
        seconds = input()

    countdownTimer(minutes, seconds)

def stopwatch():
    print('Press enter to start')
    answer = input()

    if answer == '':
        print ('test')


print('Make your choice.')
print('Timer [A]')
print('Stopwatch [B]')
print('Alarm [C]')
answer = input()

while answer != 'A' and answer != 'B' and answer != 'C':
    print('Please answer with A, B or C.')
    answer = input()

if answer == 'A':
    timer()
elif answer == 'B':
    print('Stopwatch coming soon!')
elif answer == 'C':
    print('Alarm coming soon!')



