#include<stdio.h>
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
    int flag=1;
    if(row!=colum)
    {
        flag=0;
    }
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < colum; j++)
        {
            if(i==j)
            {
                if(ar[i][j]!=1)
                {
                    flag=0;
                }
            }
            else if(ar[i][j]!=0)
            {
                flag=0;
            }
        }
    }
    if(flag==1)
    {
        printf("UNIT matrix");
    }
    else
    {
        printf("not UNIT matrix");
    }

    return 0;
}