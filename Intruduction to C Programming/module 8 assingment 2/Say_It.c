/*Problem Statement

You will be given a positive integer N. You need to print "I Want More Assignments" N times without the quotation mark. Also print from 1 to N with it. See the sample input output for more clarifications.

Input Format

Input will contain only N.
Constraints

1 <= N <= 10^5
Output Format

Output "I Want More Assignments" N times along with 1 to N and don't forget to print new line after it.
Sample Input 0
link:https://www.hackerrank.com/contests/assignment-02-a-introduction-to-c-programming-a-batch-04/challenges/say-it
*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        printf("%d. I Want More Assignments\n",i);
    }
    //printf("%d",n);
    return 0;
}