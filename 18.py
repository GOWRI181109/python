g,r=map(int,input().split())
for j in range(g+1,r):
  ch=j
  fnd=0
  while (j>0):
    s=j%10
    fnd=fnd+(s**3)
    j=j//10
    if(fnd==ch):
      print(fnd,end=" ")
