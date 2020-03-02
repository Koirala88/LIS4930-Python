
import sys
from datetime import datetime
from datetime import time
from datetime import date

def main():
    date = datetime.now()
    time = date.strftime("%X")
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 4:
            store, item, cost, payment = data
            print (f"{str(date)}\t{str(time)}\t{store}\t{item}\t{cost}\t{payment}")
        
main()

from datetime import datetime
from datetime import timedelta

def main():
      Question2()
      print("------------------------------------------")
      Question3()

def Question2():
      # Current datetime
      date = datetime.now()
      # Minus 60 seconds
      subSixtySeconds = date - timedelta(seconds = 60)
      # Add 2 years by number of days
      add2Year = date + timedelta(days = 730)
      print(f"Question #2:\nCurrent datetime: {date}\nMinus 60 seconds: {subSixtySeconds}\nAdd 2 years: {add2Year}")

def Question3():
      # Current datetime
      date = datetime.now()
      # Add 100 days
      oneHundreadDays = date + timedelta(days = 100)
      # Add 10 hours
      tenHours = date + timedelta(hours = 10)
      # Add 13 minutes
      thirteenMinutes = date + timedelta(minutes = 13)
      print(f"Question #3:\nCurrent datetime: {date}\nAdd 100 days: {oneHundreadDays}\nAdd 10 hours: {tenHours}\nAddThirteen minutes: {thirteenMinutes}")

main()
