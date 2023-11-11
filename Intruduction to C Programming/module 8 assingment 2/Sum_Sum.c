/*Problem Statement

You will be given a positive integer N and N numbers after that. You need to tell the sum of positive numbers and the sum of negative numbers separated by a space.

Input Format

First line will contain N.
Second line will contain N values named V.
Constraints

1 <= N <= 10^5
-1000 <= V <= 1000
Output Format

Output the sum of positive numbers first, then sum of negative numbers.
link:https://www.hackerrank.com/contests/assignment-02-a-introduction-to-c-programming-a-batch-04/challenges/sum-sum-2/problem*/
#include <stdio.h>
int main()
{
    int n;
    int pos = 0;
    int neg = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int v;
        scanf("%d", &v);
        if (v > 0)
        {
            pos= pos+ v;
        }
        else
        {
            neg = neg + v;
        }
    }
    printf("%d %d\n", pos, neg);

    return 0;
}