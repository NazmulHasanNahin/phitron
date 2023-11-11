#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    int a[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    int main_sum=0;
    int secondary_sum=0;
    for (int i=0;i<n;i++)
    {
        main_sum +=a[i][i];
        secondary_sum +=a[i][n-1-i];
    }
    int absvalue=abs(main_sum-secondary_sum);
    printf("%d",absvalue);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/T