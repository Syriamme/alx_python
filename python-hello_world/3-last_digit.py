import random
number = random.randint(-10000, 10000)

last = abs(number) % 10
if number < 0:
    last = -last

result = "Last digit of {} is {}".format(number, last)
if last > 5:
    result += " and is greater than 5"
elif last == 0:
    result += " and is 0"
else:
    result += " and is less than 6 and not 0"

print(result)