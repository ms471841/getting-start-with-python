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
txt="What is the most beautiful thing in this universe , simple Universe themeself  "
print("Universe" in txt)

if "beautiful" in txt:
    print("yes, 'beautiful' is present")

if "oppourtunity" not in txt:
    print("Not present")



#slicing string 
#print substring of the string b/w the given range
print(txt[3:20])    

#slice from start
print(txt[:40])

#slice from end
print(txt[10:])


#negative index
x="hello world"
print(x[-5:-2])


#Changing string to upper case using upper()

txt=txt.upper()
print(txt)

#to lower case using lower()

txt=txt.lower()
print(txt)

#remove whitespaces

txt=txt.strip()
print(txt)


#replace string

txt =txt.replace("beautiful","increidiable")
print(txt)
txt=txt.split(",")
print(txt)

#python string methods

txt="hello python users"

print(txt.capitalize())  #make the first character have upper case and the rest lower case.
print(txt.casefold())  #Return a version of the string suitable for caseless comparisons or simple in lower case
print(txt.center(3))  #Return a centered string of length width.
print(txt.count("l")) #Return the number of non-overlapping occurrences of substring sub instring 
print(txt.encode())
print(txt.endswith("users"))  #returns true if string is ended with specifeid value

#other methods cover later


#strings concatenation

#let we have 2 strings x and y
x='hello'
y='manish'
print(x+y)

#we also give the space between using ''
print(x+" "+y)

#Also we know that , we can not concatenate string and number , for example
age=20
#print(x+" "+y+" "+age)   #give me error something like this, TypeError: can only concatenate str (not "int") to str
#don't worry we have a method format(), by this we can concatenate str and int but we have to places the curley bracket where we have to add
# let do it

y='manish age {}'
print(x+ y.format(age))

#format method take unlimited methods something like that
y='manish age {} height {} number {}'
height=5.9
number=8

y='manish age {} height {} number {}'
print(x+y.format(age,height,number)) #we goona do something like that😀



#tata see in the next program 😁