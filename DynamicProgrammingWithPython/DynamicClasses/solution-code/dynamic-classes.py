#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "Classes"
lab_type = "solution-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Define functions
def function_1(self):
    print("Hello from f1()")

def function_2(self):
    print("Hello from f2()")


#CODE2: Define a new class named NewClass using the builtin type function
NewClass = type("new_class", (object,), {
    'hello1': function_1,
    'hello2': function_2,
    'color': 'red',
    'state': 'Ohio',
})

#CODE3: Instantiate the NewClass object and test it out
n1 = NewClass()
n1.hello1()
n1.hello2()
print(n1.color)
print()

#CODE4: Define a new class named SubClass which inherits from the NewClass class using the builtin type function
SubClass = type("sub_class", (NewClass,), {'fruit': 'banana'})

#CODE5: Instantiate the SubClass object and test it out
s1 = SubClass()
s1.hello1()
print(s1.color)
print(s1.fruit)
print()

