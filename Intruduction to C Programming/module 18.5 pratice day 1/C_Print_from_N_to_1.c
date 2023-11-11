#include<stdio.h>
void fun(int i,int n)
{
    if(i==0)
    {
        return;
    }
    if (i!=n)
    {
        printf(" ");
    }
    printf("%d",i);
    //printf(" ");
    fun(i-1,n);
    
}
int main()
{
    int n;
    scanf("%d",&n);
    fun(n,n);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/C