#today we gonna start data types

from ast import increment_lineno


x=int(4)
y=float(5)
z=str("manish")
xy=complex(4j)
print(x,y,z,xy)
print(type(xy))


x=list([2,3,5,6,])
y=tuple((4,5,87,4,43,7))
z=range(6)
xy=dict(name="manish",age=26)
print(x,y,z,xy)

x=set(("manish","noopur","waris","mrityunjay","satendra"))
y=frozenset(("manish","waris"))
z=bool(5)
xy=bytes(5)
print(x,y,z,xy)


#type conversion


x=int(4.6)
y=float(4)
z=str(4)
print(x,y,z)


#python string

#strings are surrounded by single or double quotes
X="hello  this is manish"
print(X)    

#multilines string


x="""Hello users this is the multiline strings
and we use triple double quotes for it
or you can use single quotes for it"""
print(x)


#string as array


x="Manish"
print(x[3])  #this will print value at indedx 3 e.i., i


#looping through the string

for x in "manish":
    print(x)

#string length
#usisng len()  function
print(len("manish"))

#check substring in a string by using 'in' keyword
txt="What is the most beautiful thing in this universe , simple Universe themeself"
print("Universe" in txt)

if "beautiful" in txt:
    print("yes, 'beautiful' is present")

if "oppourtunity" not in txt:
    print("Not present")

#tata .....see in next program😀


