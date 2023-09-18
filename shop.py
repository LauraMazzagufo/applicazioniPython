import csv # Imports the csv library

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  total = 0.0
  
  for row in reader:
    total += float((row["Cost"]))*int((row["Quantity"]))

print(f"🌟Shop $$ Tracker🌟\n Your shop took £{round(total, 2)} pounds today.")
import csv # Imports the csv library

with open("shop-totals.csv") as file: 
  reader = csv.DictReader(file) 
  total = 0.0
  
  for row in reader:
    total += float((row["Cost"]))*int((row["Quantity"]))

print(f"🌟Shop $$ Tracker🌟\n Your shop took £{round(total, 2)} pounds today.")
