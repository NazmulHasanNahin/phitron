#include <stdio.h>
int main()
{
    int a, k;
    scanf("%d %d", &a, &k);
    int arr[a];
    for (int i = 0; i < a; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < a - 1; i++)
    {
        for (int j = i + 1; j < a; j++)
        {
            if (arr[i] < arr[j])
            {
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    long long int sum = 0;
    for (int i = 0; i < k; i++)
    {
        if (arr[i] >= 0)
        {
            sum += arr[i];
        }
    }
    printf("%lld\n", sum);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/C