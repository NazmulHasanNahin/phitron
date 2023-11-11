/*Given two strings X and Y . Print the smallest lexicographical one.

Note: Lexicographical is the way of ordering the words based on the alphabetical order of their component letters.

Input
Only one line contains two strings X, Y(1 ≤ |X|, |Y| ≤ 20) consists of lowercase English letters.

Output
Print the smallest lexicographical string.

Note: If both of X and Y are equal, print any of them.
link: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/C
*/
#include <stdio.h>
#include <string.h>
int main()
{
    char a[21], b[21];
    scanf("%s %s", a, b);
    int comp = strcmp(a, b);
    if (comp < 0)
    {
        printf("%s\n", a);
    }
    else if (comp > 0)
    {
        printf("%s\n", b);
    }
    else
    {
        printf("%s\n", a);
    }

    return 0;
}