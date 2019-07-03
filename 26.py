g=int(input())
r=list(map(int,input().split()[:g]))
r.sort()
for i in r:
   print(i,end=" ")
