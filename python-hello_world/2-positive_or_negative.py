#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
   return "is positive"
elif number == 0:
  return "is zero"
else:
  return "is negative"
   
if __name__ == "__main__":
   for arg in sys.argv[1:]:
      try:
         number = int(arg)
         print(f"{number} {check_number(number)}")
      except ValueError:
         ptint(f"Invalid input: {arg} is not a valid interger.")
