		
with open("myfile.txt", "w+") as f:
    f.write("Hello World Python Programming")
    f.seek(0)
    data= f.readlines()
    count=0
    for line in data:
        words = line.split()
        if(words=="Hello"): count+=1
    print(words)
    
    print(count)          
# with open('myfile.txt', 'w+') as f:
#     # f.write("manish")
#     f.seek(0)
#     data = f.readlines()
#     for line in data:
#         words = line.split()
#         print (words)
