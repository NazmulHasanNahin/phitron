#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);   //4
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    int pos;
    scanf("%d",&pos);
    for(int i=pos;i<n-1;i++)   //1<3
    {
        ar[i]=ar[i+1]; 
    }
    for(int i=0;i<n-1;i++)
    {
        printf("%d ",ar[i]);
    }
    return 0;
}