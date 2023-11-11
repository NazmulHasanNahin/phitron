#include<stdio.h>
int main()
{
   //x=(m1*d)/(m1+m2)
   //15*5/10-day
    int n,ans,ans2;
    scanf("%d",&n);
    for(int i=0; i<n;i++)
    {
    int m1,m2,d;
    scanf("%d %d %d",&m1,&m2,&d);
    ans=(((m1*d)/(m1+m2)));
    ans2=d-ans;
    printf("%d\n",ans2);
    }
    //printf("%d\n",ans);
    return 0;
}