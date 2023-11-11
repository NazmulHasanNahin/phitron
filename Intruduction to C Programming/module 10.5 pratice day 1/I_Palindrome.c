// https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/I
#include <stdio.h>
#include <string.h>
int main()
{
    char a[1001];
    scanf("%s", a);
    int palindrome = 1;
    int leanth = strlen(a);
    for (int i = 0; i < leanth / 2; i++)
    {
        if (a[i] != a[leanth - 1 - i])
        {
            palindrome = 0;
            break;
        }
    }
    if (palindrome)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
    return 0;
}