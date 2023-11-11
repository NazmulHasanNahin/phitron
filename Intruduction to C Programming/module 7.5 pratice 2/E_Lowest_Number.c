/*Given a number N and an array A of N numbers. Print the lowest number and its position.

Note: if there are more than one answer print first one's position.

Input
First line contains a number N (2 ≤ N ≤ 1000) number of elements.

Second line contains N numbers (-105  ≤  Ai  ≤  105).

Output
Print the lowest number and its position (1-index).
link:https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E*/
#include<stdio.h>
#include<limits.h>
int main()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    int mn=INT_MAX,pos;
    for(int i=0;i<n;i++)
    {
        if(ar[i]< mn)
        {
            mn=ar[i];
            pos=i+1;
        }
    }   
    printf("%d %d\n",mn,pos);
    return 0;
}