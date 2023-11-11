#include <stdio.h>
int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    int ar[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &ar[i][j]);
        }
    }
    for (int j = 0; j < m; j++)
    {
        printf("%d ", ar[n - 1][j]);
    }
    printf("\n");
    for(int i=0;i<n;i++)
    {
        printf("%d ",ar[i][m-1]);
    }
    return 0;
}