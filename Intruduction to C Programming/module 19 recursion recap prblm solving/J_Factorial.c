#include<stdio.h>
long long int fact(long long int n)
{
    if(n==0)
    {
        return 1;
    }
    long long int ans=fact(n-1); 
    return ans*n;
}
int main()
{
    long long int n;
    scanf("%lld",&n);
    long long int res=fact(n);
    printf("%lld",res);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/J