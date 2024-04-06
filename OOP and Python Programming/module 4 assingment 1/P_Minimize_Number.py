def minimize(nmbr,n):
    count=0
    while True:
        all_even=True
        for i in range (n):
            if nmbr[i] % 2 != 0:
                all_even=False
                break
            else:
                nmbr[i]//=2
        if all_even:
            count+=1
        else:
            break
    return count
    
n=int(input())
nmbr=list(map(int,input().split()))
res=minimize(nmbr,n)
print(res)
