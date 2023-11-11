#include <stdio.h>
int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 1; i <= n; i++)
    {
        for (int a = 1; a <= k; a++)
        {
            printf("%d ", a);
        }
        printf("\n");
    }
    return 0;
}