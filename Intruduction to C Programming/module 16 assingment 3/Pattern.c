#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int s = 1;
    int k = n;
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        for (int j = 1; j < k; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= s; j++)
        {
            if (i % 2 == 0)
            {
                printf("-");
            }
            else
            {
                printf("#");
            }

        }
        if (i <= n - 1)
        {
            s += 2;
            k--;
        }
        else
        {
            s -= 2;
            k++;
        }
        printf("\n");
    }
    return 0;
}
// https://www.hackerrank.com/contests/assignment-03-a-introduction-to-c-programming-a-batch-04/challenges/pattern-255-1/submissions/code/1369821634