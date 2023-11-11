#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    scanf("%d", &n);
    while (n--)
    {
        char a[101];
        scanf("%s", a);
        int leanth = strlen(a);
        if (leanth > 10)
        {
            printf("%c%d%c\n", a[0], leanth - 2, a[leanth - 1]);
        }
        else
        {
            printf("%s\n", a);
        }
    }
    return 0;
}