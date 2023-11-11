/*Given a number N. Print the maltiplication table of the number from 1 to 12

For example: if N = 1


Input
Only one line containing a number N (1 ≤ N ≤ 50).

Output
Print 12 lines according to the required above.
input: 1
link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/F
*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=12;i++)
    {
        printf("%d * %d = %d\n",n,i,n*i);
    }
    return 0;
}