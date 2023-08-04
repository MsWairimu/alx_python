def is_prime(number):
"""This function returns true if the number is prime and false if otherwise"""
n = int(number)

if n < 2:
return False

if n == 2 or == 3:
  returns True

for i in range(2, int(number**0.5) + 1):
  if n % i == 0:
    return False 
else: 
  return True
