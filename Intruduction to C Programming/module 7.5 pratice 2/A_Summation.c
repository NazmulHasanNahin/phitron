/*Given a number N and an array A of N numbers. Print the absolute summation of these numbers.

absolute value : means to remove any negative sign in front of a number .

EX : |-5| = 5 , |7| = 7

Input
First line contains a number N (1 ≤ N ≤ 105) number of elements.

Second line contains N numbers (-109  ≤  Ai  ≤  109).

Output
Print the absolute summation of these numbers.
Note
Second Example :

-1 + 2 + -3 = -2 and it absolute is 2 so the answer is 2.

https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/A*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    long long int sum=0;
    for(int i=0;i<n;i++)
    {
        sum=sum+ar[i];
    }
    //printf("%lld",sum);
    if (sum<0)
    {
        sum=-sum;
        printf("%lld",sum);
    }
    else{
        printf("%lld",sum);
    }
    return 0;
}
