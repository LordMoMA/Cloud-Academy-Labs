#! /usr/bin/python3
import sys

sys.version_info[0]

lab_exercise = "Generators"
lab_type = "solution-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create a Generator Function that implements and yields the Fibonacci sequence
def fibonacci(max):
     a, b = 0, 1
     while a < max:
          yield a
          a, b = b, a+b

#CODE2: Iterate over the fibonacci generator function
numbers = 50
for num in fibonacci(numbers):
    print(num)

#CODE3: Use Generator Expressions to discover sum, min, and max of the square roots of a random list of numbers
import random
numbers = random.sample(range(1, 100), 20)
sumNumbers = sum(n**0.5 for n in numbers)
minNumbers = min(n**0.5 for n in numbers)
maxNumbers = max(n**0.5 for n in numbers)

#CODE4: Use f-string to format sum, min, and max
print(f"sum={sumNumbers} min={minNumbers} max={maxNumbers}")