n=int(input("Enter the limit: "))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
fib(n)