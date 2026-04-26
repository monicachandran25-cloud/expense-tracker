import csv
from datetime import datetime

def add_expense(amount, category):
    amount = float(amount)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])