number=input()
a=0
b=1
n=int(number)
if n==1:
    print(0)
else:
    for i in range(2,n):
        fb_n=a+b
        a=b
        b=fb_n
    print(b)



#using function


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            fib_n = a + b
            a = b
            b = fib_n
        return b

# Example usage
N = int(input())
print(fibonacci(N))