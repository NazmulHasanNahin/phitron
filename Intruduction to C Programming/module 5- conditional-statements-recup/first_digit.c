/*Given a number X. Print "EVEN" if the first digit of X is even number. Otherwise print "ODD".

For example: In 4569 the first digit is 4, the second digit is 5, the third digit is 6 and the fourth digit is 9.

Input
Only one line containing a number X (999 < X  ≤  9999)

link:https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/P

Output
If the first digit is even print "EVEN" otherwise print "ODD".*/
#include<stdio.h>
int main()
{
    int a;
    scanf("%d",&a);
    while(a>=10)
    a=a/10;
    if(a%2==0)
    {
        printf("EVEN");
    }
    else
    {
        printf("ODD");
    }
    return 0;
    
}