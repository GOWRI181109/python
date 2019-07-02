g=int(input())
sum=0
temp=g
while temp>0:
   digit=temp%10
   sum += digit**3
   temp//=10
if g==sum:
   print("yes")
else:
   print("no")
