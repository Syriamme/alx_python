import random
number = random.randint(-10000, 10000)

last = number % 10

output = "Last digit of {} is {}".format(number, last)
if last > 5:
    output += " and is greater than 5"
elif last == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)