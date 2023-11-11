/*Problem Statement

You will be given an integer N. If N is a positive number then print from 1 to N, otherwise print from N to 0.

Note: A positive number is a number that is strictly greater than 0.

Input Format

Input will contain only N.
Constraints

-10^5 <= N <= 10^5
Output Format

Output as asked in the question and don't forget to put a space between the values.
link:https://www.hackerrank.com/contests/assignment-02-a-introduction-to-c-programming-a-batch-04/challenges/is-it-a-challenge/problem*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    if(n>0)
    {
        for(int i=1;i<=n;i++)
        {
            printf("%d ",i);
        }
    }
    else
    {
        for(int i=n;i<=0;i++)
        {
            printf("%d ",i);
        }
    }
    return 0;
}