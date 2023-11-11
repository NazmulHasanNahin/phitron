/*https://www.hackerrank.com/contests/mid-term-a-introduction-to-c-programming-a-batch-04/challenges/count-me-2-1*/
#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int a[n];
    int divisible_2 = 0;
    int divisible_3 = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        if (a[i] % 2 == 0)
        {
            // printf("%d ",a[i]);
            divisible_2++;
        }
        else if (a[i] % 3 == 0)
        {
            divisible_3++;
        }
    }
    printf("%d %d",divisible_2,divisible_3);
    return 0;
}