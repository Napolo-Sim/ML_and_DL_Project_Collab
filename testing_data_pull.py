from data import data

first_10 = [data["prices"][x] for x in range(10)]

for day in first_10:
    print(day)