import datetime
import B_Day_Messages # type: ignore

today = datetime.date.today()
next_birthday = datetime.date(2025, 3, 17)


days_away = today - next_birthday

if (days_away == 0):
    print(B_Day_Messages.random_message)
else:
    print('My next birthday is ' + str(days_away) + ' days away!')

