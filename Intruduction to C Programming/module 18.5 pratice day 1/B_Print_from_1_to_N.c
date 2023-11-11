#include<stdio.h>
void fun(int i,int n)
{
    // int i;
    if (i==n) return;
    printf("%d\n",i);

    fun(i+1,n);
}
int main()
{
    int n;
    scanf("%d",&n);
    fun(1,n+1);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/B