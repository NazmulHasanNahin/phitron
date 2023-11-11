/*Given a number N and an array A of N numbers. Print the array after doing the following operations:

Find minimum number in these numbers.
Find maximum number in these numbers.
Swap minimum number with maximum number.
Input
First line contains a number N (2 ≤ N ≤ 1000) number of elements.

Second line contains N numbers ( - 105 ≤ Ai ≤ 105)

It's guaranteed that all numbers are distinct.

Output
Print the array after the replacement operation.
link:https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
*/
#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    int minimum_value=a[0];
    int maximum_value=a[0];
    int min_index=0;
    int max_index=0;
    for (int i=0;i<n;i++)
    {
        if(a[i]<minimum_value)
        {
            minimum_value=a[i];
            min_index=i;
        }
        if(a[i]>maximum_value)
        {
            maximum_value=a[i];
            max_index=i;
        }
    }
    int temp=a[min_index];
    a[min_index]=a[max_index];
    a[max_index]=temp;
    for(int i=0;i<n;i++)
    {
        printf("%d ",a[i]); 
    }
    return 0;
}