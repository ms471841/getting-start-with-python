#Boolean in python

print(10>9)
print(10>23)
print(10==9)
print(10==10)


x=10


if x>5:
    print('x is greater than 5')
else:
    print('less than 5')


print(bool(0))
print(bool(1))
print(bool(None))
print(bool({}))
print(bool('str'))
print(bool(0.0))
print(bool(0.5))
print(bool())


def myName():
    return True
print(myName())   