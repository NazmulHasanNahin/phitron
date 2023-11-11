#include <stdio.h>
int main()
{
    int row, colum;
    scanf("%d %d", &row, &colum);
    int element=row*colum;
    int ar[row][colum];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < colum; j++)
        {
            scanf("%d", &ar[i][j]);
        }
    }
    int count = 0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < colum; j++)
        {
            if (ar[i][j]==0)
            {
                count++;
            }
        }
    }
    //printf("%d\n",count);
    if (element==count)
    {
        printf("SAME");
    }
    else
    {
        printf("Not same");
    }
    return 0;
}