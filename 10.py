#display all prime number within a range between 15 and 45
a=15
b=45
for n in range(a,b+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=" ")