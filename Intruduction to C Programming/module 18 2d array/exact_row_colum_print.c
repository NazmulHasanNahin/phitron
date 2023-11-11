#include<stdio.h>
int main()
{
    int row,colum;
    scanf("%d %d",&row,&colum);
    int ar[row][colum];
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<colum;j++)
        {
            scanf("%d",&ar[i][j]);
        }
    }
    //exat colum
    // int excat=2;
    // for(int i=0;i<colum;i++)
    // {
    //     printf("%d ",ar[excat][i]);
    // }
    int excat=1;
    for(int i=0;i<row;i++)
    {
        printf("%d ",ar[i][excat]);             //exat colum;
    }
    return 0;
}