#include<stdio.h>
int main()
{
    int tst;
    scanf("%d",&tst);
    for(int t=0;t<tst;t++)
    {
        int n;
        scanf("%d",&n);
        char ar[n+1];
        scanf("%s",ar);
        int patan=0,tiger=0;
        for (int i=0;i<n;i++)
        {
            if(ar[i] == 'T')
            {
                tiger++;
            }
            else if(ar[i]=='P')
            {
                patan++;
            }
        }
        if (patan>tiger)
        {
            printf("Pathaan\n");
        }
        else if(tiger>patan)
        {
            printf("Tiger\n");
        }
        else
        {
            printf("Draw\n");
        }
    }
    return 0;
}