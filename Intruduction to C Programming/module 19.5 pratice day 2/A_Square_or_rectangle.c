#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int w,h;
        scanf("%d %d",&w,&h);
        if (w==h)
        {
            printf("Square");
        }
        else
        {
            printf("Rectangle");
        }
        printf("\n");
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/A