#include<stdio.h>
int main()
{
    long long int e,m,b, res=0;
    scanf("%lld %lld %lld",&e,&m,&b);
    if (e==0 || b==0)
    {
        printf("0");
    }
    else
    {
        long long int mn=e;
        if(m<mn)
        {
            mn=m;
        }
        if(b<mn)
        {
            mn=b;
        }
        res+=mn;
        e-=mn;
        b-=mn;
        m-=mn;
        if(e/2 < b)
        {
            res+=e/2;
        }
        printf("%lld",res);  
    }
    return 0;
}