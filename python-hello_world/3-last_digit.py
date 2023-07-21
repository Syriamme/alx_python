import random
number = random.randint(-10000, 10000)

last = abs(number) % 10

results = "Last digit of {} is {}".format(number, last)
if last > 5:
    results += " and is greater than 5"
elif last == 0:
    results += " and is 0"
else:
    results += " and is less than 6 and not 0"

print(results)