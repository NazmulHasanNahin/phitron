/*Given a number N. Print all even numbers between 1 and N inclusive in separate lines.

Input
Only one line containing a number N (1 ≤ N ≤ 103).

link:https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/B

Output
Print the answer according to the required above. If there are no even numbers print -1.*/
#include<stdio.h>
int main()
{
    int a,n;
    scanf("%d",&n);
    if(n==1)
    {
        printf("-1\n");
    }
    for(a=2;a<=n;a+=1)
    {
        if(a%2==0)
        {
            printf("%d\n",a);
        }
    }
    return 0;
}