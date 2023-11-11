#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int ar[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &ar[i]);
    }
    int min = ar[0];
    int cnt = 1;
    for (int i = 1; i < n; i++)
    {
        if (ar[i] < min)
        {
            min = ar[i];
            cnt = 1;
        }
        else if (ar[i] == min)
        {
            cnt++;
        }
    }
    if (cnt % 2 == 1)
    {
        printf("Lucky\n");
    }
    else
    {
        printf("Unlucky\n");
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/J