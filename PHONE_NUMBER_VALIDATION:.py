n=int(input())
x=n
c=0
if x%1000000000>0:
    s=str(n)
    if len(s)==10:
        print("Valid")
    else:
        print("Invalid")
    
else:
    print("Invalid")
    