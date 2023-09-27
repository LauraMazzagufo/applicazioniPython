#events countdown timer. Your program should:
# 1. Austomatically work out today's date.
# 2. Prompt the user to input the name and date of their event (year, month and day).
#3. Work out the number of days until the event and output it.
#4. If the event is happening today, insert some party emojis.
#5. If the event was in the past, sad face emojis and tell the user how many days ago it was.

import datetime
print("🌟Event Countdown Timer🌟")

name = str(input("Input the event: > "))
eventYear = int(input("Input the year > "))
eventMonth = int(input("Input the month > "))
eventDay = int(input("Input the day > "))

today = datetime.date.today() 
event = datetime.date(year = eventYear, month = eventMonth, day = eventDay)

if event == today: 
  print(f"🎉🎉 {name} is today! 🎉🎉")
elif event < today: 
  print("😭😭😭😭😭 Hope you enjoyed it")
else:
  daysToGo = event - today
  daysToGo = daysToGo.days
  print(f"{name} running in {daysToGo} days!")