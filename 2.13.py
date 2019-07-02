raj=int(input())
if (raj<=1000):
   for i in range(2,raj):
       if(raj%i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
