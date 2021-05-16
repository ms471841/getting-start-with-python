#today we gonna start list in python
#list are ordered , changeable, allow duplicates

lst=[]  #this is empty list , a list is create by square brackets
print(lst)

#list items eithers numbers or strings or both i.e., alphanumerical
lst=[2,4,5,6]
print(lst)


lst=['artificial intelligence','machine learning','flutter','block chain','deep learning']
print(lst)

lst=['artificial intelligence','machine learning','flutter',6,'block chain','deep learning',4,7,7,4]
print(lst)

#element accessing 
print(lst[4]) #at index 4 block chain will be print
#note , index start at 0

#negative indexing 
#negative indexing start from the end side last element of the list is at index -1 then second last -2 , third last -3 and so on

print(lst[-1])
print(lst[-2])


#range based indexing 

print(lst[0:5])

print(lst[-5:-1])


#changing list item

lst[1]='changes done'
print(lst)

lst[0:2]='changes done','to','here'
print(lst)
lst[3:5]='newstarting'
print(lst)

#insert item

lst.insert(2,'insert item')




#append function is used to add new item in the list where as list is ordered so item is append at the end of list
lst.append('added')
print(lst)




