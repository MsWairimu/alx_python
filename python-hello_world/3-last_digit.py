#!/usr/bin/python3
import random

def check_number_last_digit(number):
    last_digit = abs(number) % 10

    if last_digit > 5:
        return "and is greater than 5"
    elif last_digit == 0:
        return "and is 0"
    else:
        return "and is less than 6 and not 0"
    else:
    return "and is negative"

number = random.randint(-10000, 10000)
number_str = str(number)

last_digit_of_string = number_str[-1]
number_part = number_str[:-1]
last_digit_of_number = abs(number) % 10

output = f"Last digit of {number} is {last_digit_of_number} {check_number_last_digit(number)}"
print(output)
