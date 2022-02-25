from datetime import datetime
from playsound import playsound
print('Hi, this is alarm clock!')
print('Please, enter time in format:  hh:mm')
ttime = input('Time: ')
hour = int(ttime[:2])
minute = int(ttime[3:])
while True:
    current_datetime = datetime.now()
    if current_datetime.hour == int(hour) and current_datetime.minute == int(minute):
        try:
            playsound('alarm.mp3') 
        except:
            print()
        break
