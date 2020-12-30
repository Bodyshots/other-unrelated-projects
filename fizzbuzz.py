# Fizzbuzz
import math
import sys
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 3 != 0 and i % 5 != 0:
        output += str(i)
    print(output.capitalize())
