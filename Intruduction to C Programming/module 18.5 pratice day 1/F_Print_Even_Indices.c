#include <stdio.h>
void fun(int ar[], int n, int i)
{
    if (i < 0)
    {
        return;
    }
       
    if (i % 2 == 0)
    {
        printf("%d ", ar[i]);
    }
    fun(ar, n, i - 1);
}
int main()
{
    int n;
    scanf("%d", &n);
    int ar[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &ar[i]);
    }
    fun(ar, n - 1, n - 1);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/F