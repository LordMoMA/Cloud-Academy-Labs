#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Lambdas"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Use Lambda and Map to double numbers in a list
list = [1, 2, 3, 4]

result = map(lambda x: x * 2, list)  
print(result)



#CODE2: Use Lambda and Filter to split list of numbers into odds and evens

evens = filter(lambda x: x % 2 == 0, list)
odds = filter(lambda x: x % 2 != 0, list)