#!/usr/bin/python3
import csv
with open("data.csv", "r", encoding="UTF-8") as csvfile:

    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
