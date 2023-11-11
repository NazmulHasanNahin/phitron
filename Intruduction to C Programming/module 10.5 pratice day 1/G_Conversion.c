/*Given a string S. Print the origin string after replacing the following:

Replace every comma character ',' with a space character.
Replace every capital character in S with its respective small character and Vice Versa.
Input
Only one line contains a string S (1 ≤ |S| ≤ 105) where |S| is the length of the string and it consists of lower and upper English letters and comma character ','.

Output
Print the string after the conversion.
link:https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/G
*/
#include <stdio.h>
#include <string.h>
int main()
{
    char a[100001];
    scanf("%s", a);
    int leanth = strlen(a);
    for (int i = 0; i < leanth; i++)
    {
        if (a[i] == ',')
        {
            a[i] = ' ';
        }
    }
    for(int i=0;i<leanth;i++)
    {
        if(a[i]>='a' && a[i]<='z')
        {
            a[i]=a[i]-32;
        }
        else if(a[i]>='A' && a[i] <= 'Z')
        {
            a[i]=a[i]+32;
        }
    }
    printf("%s", a);
    return 0;
}