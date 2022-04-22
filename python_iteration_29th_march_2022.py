##var = "India is my country"
##for x in var:
##    print(x)    # Here we are using loop to travel in the var and the output is printed in different line
    
# To print the data in same line we are using the syntax below  
##var = "India is my country"
##for x in var:
##    print(x,end = "")

#for having space between letters or having some characters in between

##var = "India is my country"
##for x in var:
##    print(x,end = " ")
    
##var = "India is my country"
##for x in var:
##    print(x,end = " &")
    
##var = "India is my country"
##for x in var:
##    print(x,end = " *")

#For loop for lists,string as they can be accessed using index value
##var = "India is my country"
##for x in enumerate(var):
##    print(x)
#In output we can see that each letter comes with their index value.
# enumerate is used for two values.

##var = "India is my country"
##for x,y in enumerate(var):
##    print(x)
##    print(y)
# x is to store the index value
# y is used to store letter

##var = "India is my country"
##for x,y in enumerate(var):
##    print(x,end = "")
##    print(y,end = "") # here we can see in output both index and their corresponding letter will be printed in same line.

# Without using len function how to calculate the length is diiscussed between line no 45 to 50.  

##var = "India is my country"
##my_counter = 0
##for x in var:
##    print(x)
##    my_counter = my_counter+1
##print(my_counter)

##var = "India is my country"
##for x in var:
##    if x =="I":
##        print(x,"success")
##    else :
##        print(x,"failure")

# if can be used alone also
##var = "India is my country"
##if var == "India is my country" :
##    print(var)
##else :
##    print("not found")


##var = "India is my country"
##for x in var:
##    if x== "I":
##        print("success")
##    elif x == "n":
##        print("success")
##    else:
##        print("failure")
    
# we can use or function to optimize the code

##var = "India is my country"
##for x in var:
##    if x == "I" or x == "n":
##        print(x,"success")
##    else :
##        print(x,"failure")

var =  ["age","dhoni",33,2.57]
for i in var:
    if i == var[4]:
        print("found")
else:
    print("not found")



##var = "India is my country"
##for x in var:
##    if x == "i" or x == "n":
##        print("success")
##        break
# break is used to terminate the for loop or we can say it just helps in comin out of the loop.   
        
##var = "India is my country"
##for x in var:
##    if x == "I" or x == "n":
##        print("success")
##        break
##    else :
##        print("failure")
    
##var = "India is my country"
##for x in var:
##    if x == "I" or x == "n":
##        print("success")
##        continue
##        print("failure")

##print("What is your age")
##age = int(input())
##if age > 18:
##    print("Yes he can drive")
##elif age == 18:
##    print("come pyhsically teh we will decide")
##else:
##    print("Not eligible to drive")

##
##print("Which exam you passed")
##subject = int(input())
##if subject >= 5:
##    print("You got 50rs as award")
##elif subject == 4:
##    print("You got Rs 45 as award")
##elif subject >= 3:
##    print("You got Rs 30 as award") 
##else: 
##    print("You got a certificate")
    
##subject = "Maths"+"Science"
##print(subject)








    
        



