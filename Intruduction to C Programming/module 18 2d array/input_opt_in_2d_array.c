#include<stdio.h>
int main()
{
    int ar[5][3];
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<3;j++)
        {
            scanf("%d",&ar[i][j]);
        }
    }
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d ",ar[i][j]);
        }
        printf("\n");
    }
    return 0;
}




