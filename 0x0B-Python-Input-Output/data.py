#!/usr/bin/python3
import csv
with open("data.csv", "r", encoding="UTF-8") as csvfile:
    store = []
    reader = csv.DictReader(csvfile, fieldnames= ["id", "name", "manager", "location"])
    for row in reader:
        store.append(row)

    for row in store:

        writer.writerrow({"id": ["id"], "name": ["name"], "manager": ["manager"], "location": ["location"]})
