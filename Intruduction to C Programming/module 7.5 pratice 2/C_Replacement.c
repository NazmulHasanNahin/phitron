/*Given a number N and an array A of N numbers. Print the array after doing the following operations:

Replace every positive number by 1.
Replace every negative number by 2.
Input
First line contains a number N (2 ≤ N ≤ 1000) number of elements.

Second line contains N numbers (-105  ≤  Ai  ≤  105).

Output
Print the array after the replacement and it's values separated by space.
link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/C
input:5
1 -2 0 3 4
*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d\n",&ar[i]);
    }
    for(int i=0;i<n;i++)
    {
        if(ar[i]>0)
        {
            printf("1 ");
        }
        else if(ar[i]==0)
        {
            printf("0 ");
        }
        else
        {
            printf("2 ");
        }
    }
    return 0;
}