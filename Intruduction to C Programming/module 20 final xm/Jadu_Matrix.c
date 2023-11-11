#include<stdio.h>
int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    int ar[n][m];
    for (int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            scanf("%d",&ar[i][j]);
        }
    }
    int flag=1;
    for(int i=0;i<n && flag;i++)
    {
        for(int j=0;j<m;j++)
        {
            if((i==j || i+j==n-1) && ar[i][j]!=1)
            {
                flag=0;
                break;
            }
            if(i!=j && i+j !=n-1 && ar[i][j] !=0)
            {
                flag=0;
                break;
            }
        }
    }
    if (flag)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
    return 0;
}