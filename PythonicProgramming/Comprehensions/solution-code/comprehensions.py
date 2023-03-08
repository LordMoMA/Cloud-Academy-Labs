#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Comprehensions"
lab_type = "solution-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Create a list with various elements and then define a list comprehension that filters on it
randomChars = ['a', 0, -3, 10, 4, 'p', '>', 7]
squaresList = [ x**2 for x in randomChars if type(x) == int ]
print(squaresList)

#CODE2: Create a list with various animal names and then define a set comprehension that filters on it
animalsList = [ 'whale', 'TIGER', 'lion', 'lion', 'X', 'ELEPHANT', 'cheetah', 'cat', 'DOG', 'W' ]
animalsSet = { animal[0].upper() + animal[1:].lower() for animal in animalsList if len(animal) > 1 }
print(animalsSet)

#CODE3: Create a dict of square roots and then iterate of the items printing out each key-value pair
squareRoots = {x : x**0.5 for x in range(1,20)}
for idx, squareRoot in squareRoots.items():
    print(f'{idx}->{squareRoot:.3f}')


