#include<stdio.h>
int summation(int a,int b)
{
    int sum=a+b;
    return sum;
}
int main()
{
    int a,b;
    scanf("%d %d", &a, &b);
    int result =summation(a,b);
    printf("%d\n",result);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/A