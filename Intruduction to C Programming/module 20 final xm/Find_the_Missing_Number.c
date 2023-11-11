#include<stdio.h>
int main()
{
    int tst;
    scanf("%d",&tst);
    for(int i=0;i<tst;i++)
    {
        long long int m,a,b,c;
        scanf("%lld %lld %lld %lld",&m,&a,&b,&c);
        long long int x= m/(a*b*c);
        long long int res=(a*b*c*x);
        if (res==m)
        {
            printf("%lld\n",x);
        }
        else
        {
            printf("-1\n");
        }
    }
    return 0;
}