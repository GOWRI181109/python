gv,rj=map(int,input().split())
for r in range(gv+1,rj,1):
    if(s>1):
        for a in range(2,s):
            if(s%a==0):
                break
        else:
            print(s,end=" ")
