/*outputstandard output
Given a number N and an array A of N digits (not separated by space). Print the summation of these digits.

Input
First line contains a number N (1  ≤  N  ≤  106) number of digits.

Second line contains N digits (0 ≤ Ai ≤ 9).

Output
Print the summation of these digits.link:https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    char digit;
    int sum=0;
    for(int i=0;i<n;i++)
    {
        scanf(" %c",&digit);
        sum+=digit-'0';
    }
    printf("%d\n",sum);
    return 0;
}