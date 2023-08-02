#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
   return "is positive"
elif number == 0:
  return "is zero"
else:
  return "is negative"

