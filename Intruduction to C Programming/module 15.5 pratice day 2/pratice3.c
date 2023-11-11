#include<stdio.h>
int count_odd(int ar[],int n)
{
    int count=0;
    for(int i=0;i<n;i++)
    {
        if(ar[i]%2!=0)
        {
            count++;
        }
    }
    return count;
}
int main()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    int res=count_odd(ar,n);
    printf("%d",res);
    return 0;
}