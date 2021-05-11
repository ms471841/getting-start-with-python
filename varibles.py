#variables in python



#we can declare a variable by assign a value to it...
x=10   #x is a varibles which holds value 10  and is type is int
print(x)  #value of x will be print

x='10' #value of x will be overwrite by '10' and type is str
print(x)

x=10.0 #value of x will be overwrite by 10.0 and type is double
print(x)

#we can give explicit the data type to a varible by casting

x=str (10)  #value of x is str type 
print(x)

x=int(20.0)   #value of x will be int type
print(x)

x=float (30)#value of x will be float type
print (x)

#we also get the datatype of any varible by using type()

x=10
print(type(x))
x='manish'
print(type(x))

#we also get for others 

#Varibles name 
"""varible name should start with the letter or underscore 
     can not start with the number 
   python is case sensetive ...age or Age are 2 diff variables
"""
myNameVariable="manish saini"   #camle case variable
print(myNameVariable)
my_name_variable="noopur garg"   #snake case variable
print(my_name_variable)
MyNameVariable="waris ali"   #pascal case variable
print(MyNameVariable)


#many variablrie to multiple variable
#varible must match to the no of values
x,y,z="manish","noopur","waris"
print(x)
print(y)
print(z)

#unpack Collection

name=["manish","noopur","waris"]
x,y,z=name
print(x)
print(y)
print(z)

print(x+y)
print(x+y+z)
a=9
#print(z+a)    #give the error


#gloable variable  is the variable that declare the outside the function
x="gloable  manish"
def myName():
    
    print(x)
myName()    


x="gloable manish"
def myName():
    x="local manish"
    print(x)
myName()


#tata see you in the next program




