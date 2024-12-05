number_days = int(input("Enter the number of days: "))
total = 0
temp = []
for i in range(1, number_days+1):
    temp = float(input(f"Enter the temperature for day {i}: "))
    total += temp[i]

average = round(total / number_days, 2)
print(f"Average temperature: {average}")
above = 0
for i in temp:
    if i > average:
        above += 1
print(f"Number of days above average: {above}")