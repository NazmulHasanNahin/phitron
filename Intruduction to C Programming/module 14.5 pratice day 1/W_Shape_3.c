// https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/W
#include <stdio.h>
int main()
{
    int n, s, k = 1;
    scanf("%d", &n);
    s = n - 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= s; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= k; j++)
        {

            printf("*");
        }
        s--;
        k += 2;
        printf("\n");
    }
    int N;
    N=n;
    for (int i = N; i >= 1; i--)
    {
        for (int j = 1; j <= N - i; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= 2 * i - 1; j++)
        {
            printf("*");
        }
        s++;
        k -= 2;
        printf("\n");
    }
    return 0;
}