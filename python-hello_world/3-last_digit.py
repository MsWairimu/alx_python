#!/usr/bin/python3
import random 
number = random.randint(-10000, 10000)

def check_number_last_digit(number):
    last_digit = abs(number) % 10

    if last_digit > 5:
        return "and is greater than 5"
    elif last_digit == 0:
        return "and is 0"
    else:
        return f"is less than 6 and not 0"

number_str = str(number)

last_digit_of_string = number_str[-1]
number_part = number_str[1:-1]
last_digit_of_number = abs(number) % 10

output = f"-{last_digit_of_string}, followed by\n" \
         f"-{number_part}, followed by\n" \
         f"-the string is, followed by\n" \
         f"-the last digit of number, {last_digit_of_number}, {check_number_last_digit(number)}"

print(output)
