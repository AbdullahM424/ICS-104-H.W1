##
# This program implements the 3 logic functions: and, or, not without using the (and, or, not) operators.
#
#

# YOUR CODE HERE
LogicFunction=str(input("Enter logic function anme(and, or, not): ")) # The logic function that we want to use it. notice that the range must be (and,or,not).
# Anything else will not excute the A Input.
     
if LogicFunction=="and":  # In this condition if  we use "and" 
    A= str(input("Enter value of condition A: "))  #The A input we put it inside condition of LogicFunctoin  and the range must be(0,1)
    if A=="0":                          # The range of A and B must be (0,1)
        B= str(input("Enter value of ccondition B: "))     #The B input we put it inside condition of A because if the range of "A"is not 0 or 1 then it will not print the condition of B
        if B=="0":
            print('"and" logic function result=0')
        elif B=="1":
              print('"and" logic function result=0')  
        else:    #Here if the input B not 0 or 1 then will execute the below condition
            print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
    elif A=="1":
            B= str(input("Enter value of ccondition B: "))
            if B=="0":
                print('"and" logic function result=0')
            elif B=="1":
                print('"and" logic function result=1')
            else :   #Here if the input B not 0 or 1 then will execute the below condition
                print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
    else:
        print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")    

elif LogicFunction=="or":     # In this condition if  we use "or" 
    A= str(input("Enter value of condition A: "))   #The A input we put it inside condition of LogicFunctoin "or" the range must be(0,1) 
    if A=="0":                                # The range of A and B must be (0,1)
        B= str(input("Enter value of ccondition B: "))     #The B input we put it inside condition of A because if the range of "A"is not 0 or 1 then it will not print the condition of B 
        if B=="0":
            print('"or" logic function result=0')
        elif B=="1":
            print('"or" logic function result=1')
        else:        #Here if the input B not 0 or 1 then will execute the below condition
            print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
    elif A=="1":
            B= str(input("Enter value of ccondition B: "))
            if B=="0":
                print('"or" logic function result=1')
            elif B=="1":
                print('"or" logic function result=1')
            else:       #Here if the input B not 0 or 1 then will execute the below condition
                print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
    else:
        print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
    
        
elif LogicFunction=="not":      #Here use the "not" condition  notice that we don't have B input
    A= str(input("Enter value of condition A: "))   #The A input we put it inside condition of LogicFunctoin "not" the range must be(0,1
    if A=="0":                          # if A equal to zero then it will print 1 and the oppsite
        print('"not" logic function result=1')
    elif A=="1":
        print('"not" logic function result=0')
    else:              #Here if the input A not 0 or 1 then will execute the below condition
        print("Error: either B is not a digit, has more than one digit, or is out of the 0,1 range")
else:    # if the LogicFunction not 0 or 1 then it will execute the below condition
    print("Error: unknown logic function")
    
            
            
            
            
