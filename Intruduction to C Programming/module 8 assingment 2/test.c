/*Problem Statement

You will be given a positive integer N and an array A of size N. Suppose, the index starts from 0, then you need to print all the values at odd indexes in reverse way.

For example:

If the input is

6
10 20 30 40 50 60
You need to print 60 40 20 as their indexes are 5 3 1 respectively.

Input Format

First line will contain N.
Second line will contain the array A.
Constraints

1 <= N <= 10^5
1 <= A[i] <= 1000 ; where A[i] are the values of array A.
Output Format

Output the values of odd indexes in reverse way. Don't forget to put a space between two values.
link:https://www.hackerrank.com/contests/assignment-02-a-introduction-to-c-programming-a-batch-04/challenges/reverse-and-odd*/
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
    for(int i=n-1;i>=0;i--)
    {   if(i%2==1)
        {
            printf("%d ",ar[i]);
        }
    }
    return 0;
}