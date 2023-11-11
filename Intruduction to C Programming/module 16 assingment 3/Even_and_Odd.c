#include<stdio.h>
void odd_even()
{
    int n;
    scanf("%d",&n);
    int ar[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    int odd_cnt=0;
    int even_cnt=0;
    for(int i=0;i<n;i++)
    {
        if(ar[i]%2==0)
        {
            even_cnt++;
        }
        else
        {
            odd_cnt++;
        }
    }
    printf("%d %d\n",even_cnt,odd_cnt);
}
int main()
{
    
    odd_even();
    return 0;
}