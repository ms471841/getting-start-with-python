import time
startTime=time.time()
r=int(input("Enter upper limit: "))
print(2)
for a in range(2,r+1):
 k=0
 if(a%2==0):
     continue
 for i in range(2,a//2+1):
  if(a%i==0):
   k=k+1
 if(k<=0):
  print(a)
print("--- %s seconds ---" % (time.time() - startTime))