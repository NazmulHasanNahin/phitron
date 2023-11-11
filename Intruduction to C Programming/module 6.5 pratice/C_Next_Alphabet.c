/*Given a lowercase alphabet character. You have to print the next character in the alphabet.

Input
Only one line containing a lowercase English letter C
.

Output
Print the next letter to C
 in the alphabet.
 link:https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/C
 input:a

*/
#include<stdio.h>
int main()
{
    char h;
    int x;
    scanf("%c",&h);
    if(h=='z')
    {
        printf("a");
    }
    else if(h>='a' || h<='z')
    {
        printf("%c",x=h+1);
    }
    return 0;
}