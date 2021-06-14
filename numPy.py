#Implementing numpy libary (module)

import numpy as np
from numpy.core.fromnumeric import mean, std, var
from numpy.core.records import array
from numpy.lib.function_base import median

arr1 = np.array([1, 2, 3, 4, 5])
arr2=np.array([[2,3],[2,6],[4,8,]])
arr3=np.array([[[3,4],[5,7]],[[6,4],[7,4]]])
print(f"1- D array is: {arr1} of dimension {arr1.ndim}")
print(f"array type:  {type(arr1)}")
print(f"2- D array is :\n{arr2} of dimension {arr2.ndim}")
print(f"3-D array is :\n{arr3} of dimension {arr3.ndim}")

arrn=np.array([2,4,6,7,8,9,],ndmin=5)
print(f"{arrn} of dimension {arrn.ndim}")

np.append(arr1,6)
print(f"after append 6 in arr1 :{arr1}")
#array indexing

print(arr1[3])
print(arr1[2]+arr1[4])
print(arr2[2])
print(arr3[1])
print(arr2[1,1])
print(arr3[0,1,1])
print(arrn[0,0,0,0,3])
print(arr2[0,-1])


#array slicing

print(arr1[1:4])
print(arr3[1:])

print(f"2 d array slicing :{arr3[1,1:]}")
print(f"2 d array slicing :{arr3[1,1,0:]}")

print(arr3.dtype)

arr=np.array(["C","C++","python","flutter + dart", "SQL"," Data structure & algo"],dtype='S')
print(arr)

print(arr.dtype)

#aray joinning
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.concatenate((v1,v2))
print(v3)

#split the array

print(np.array_split(v3,3))


#searching

print(np.where(v3%2==0))  #retrun array index

print(np.searchsorted(v3,3,side="right"))

# mean , median , variance , std dev


data=np.array([3,6,9,12,15,18,21,24,27,30])
print(f"mean: {mean(data)}")
print(f"median: {median(data)}")
print(f"standard deviation : {std(data)}")
print(f"variance : {var(data)}")

