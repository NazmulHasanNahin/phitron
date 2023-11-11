#include<stdio.h>
int main()
{
    int a,n;
    scanf("%d",&n);
    for(a=2;a<=n;a+=1)
    {
        if(a%2==0)
        {
            printf("%d",a);
        }
    }
    return 0;
}