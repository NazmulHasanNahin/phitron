#include <stdio.h>
void change_it(int ar[], int n, int chng_value)
{
    if(n>0)
    {
        ar[n-1]=chng_value;
    }
}
int main()
{
    int n;
    scanf("%d\n", &n);
    int ar[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&ar[i]);
    }
    int chng_value=100;
    change_it(ar,n,chng_value);
    for(int i=0;i<n;i++)
    {   
        printf("%d", ar[i]);
        if(i <n-1)
        {
            printf(" ");
        }
    }
    return 0;
}