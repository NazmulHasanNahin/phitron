/*A number of two digits is lucky if one of its digits is divisible by the other.

For example, 39, 82, and 55 are lucky, while 79 and 43 are not.

Given a number between 10 and 99, determine whether it is lucky or not.

Input
Only one line containing a single number N
 (10≤N≤99)
.

Output
Print "YES" if the given number is lucky, otherwise print "NO".
link:https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/I
input:39

*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int a,b;
    a=n%10;
    b=n/10;
    if(a%b==0 || b%a==0)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
    return 0;
}