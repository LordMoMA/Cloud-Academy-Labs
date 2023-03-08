#! /usr/bin/python3
import sys
sys.version_info[0]

lab_exercise = "MonkeyPatching"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE2: Import the monk module

#CODE3: Create monkey patch function
   
#CODE4: Apply monkey patch function replacing address of "func" with "monkey_f" 

#CODE5: call function "func" whose address got replaced with function "monkey_f()" 
