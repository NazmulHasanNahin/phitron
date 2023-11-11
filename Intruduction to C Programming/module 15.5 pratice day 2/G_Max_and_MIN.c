#include<stdio.h>
void func(int ar[],int n,int *min,int *max)
{
    *min=*max=ar[0];
    for(int i=1;i<n;i++)
    {
        if(ar[i]> *max)
        {
            *max=ar[i];
        }
        if(ar[i]< *min)
        {
            *min=ar[i];
        }
        
    }
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
    int min,max;
    func(ar,n,&min,&max);
    printf("%d %d\n",min,max);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/G