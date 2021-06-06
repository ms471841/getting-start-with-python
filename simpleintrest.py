#program to calculate the simple intrest

p,r,t=[int (x) for x in input("enter principle , rate and time:").split()]
print(f"simple intrest :{p*r*t/100}")