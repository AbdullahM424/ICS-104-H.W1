##
# This program computes 3 norm distances for 2 points in the plane.
#

# YOUR CODE HERE
from math import*              # we must use math library to use the "sqrt" and abs"
NormName= str(input("Enter desired norm name (infinity, 1-norm, 2-norm): ")) # This input we must choose one of the three norm name. Anything else will print error 

if NormName =="infinity":     
    Value_x1= float(input("Enter value of coordinate value x1: "))  
    Value_y1= float(input("Enter value of coordinate value y1: "))
    Value_x2= float(input("Enter value of coordinate value x2: "))    # Here we have the  value of coordinates x and y
    Value_y2= float(input("Enter value of coordinate value y2: "))
    infinity= max(abs(Value_x1-Value_x2),abs(Value_y1-Value_y2))  # The rule of infinity we use it if  we put in the first input "infinity"
    print("Infinity-norm distance value =",infinity)    #from the rule we will take the max number to find the distance
elif NormName =="1-norm":
    Value_x1= float(input("Enter value of coordinate value x1: "))
    Value_y1= float(input("Enter value of coordinate value y1: "))
    Value_x2= float(input("Enter value of coordinate value x2: "))     # Here we have the  value of coordinates x and y
    Value_y2= float(input("Enter value of coordinate value y2: "))
    norm1= abs(Value_x1-Value_x2)+abs(Value_y1-Value_y2)       # The rule of 1-norm we use it if we put in the fisrt input "1-norm"
    print("1-norm distance value =",norm1)    #from the rule we will take the diffrent from "x" and "y" and add the numbers to find the distance
elif NormName =="2-norm":
    Value_x1= float(input("Enter value of coordinate value x1: "))
    Value_y1= float(input("Enter value of coordinate value y1: "))
    Value_x2= float(input("Enter value of coordinate value x2: "))     # Here we have the  value of coordinates x and y
    Value_y2= float(input("Enter value of coordinate value y2: "))
    norm2= sqrt((Value_x1-Value_x2)**2+(Value_y1-Value_y2)**2)    # The rule of 2-norm we use it if we put in the fisrt input "2-norm"
    print("2-norm distance value =","%.2f"%norm2)               #from the rule we will take the diffrent from "x" and "y" and add the numbers to find the distance
else:
    print("Error: unknown norm")   #Here if you notice that in the first input "NormName" that we said if it's not one of them it will print error. The condition below that what will print.
