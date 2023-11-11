#include <stdio.h>
int main()
{
    int test;
    scanf("%d", &test);
    int n, s, k = 1;
    n = ((test - 1) / 2) + 6;
    // scanf("%d", &n);
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
        printf("\n");
        s--;
        k += 2;
    }
    int N = 5; 
    //int test = 1; 

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 5; j++) {
            printf(" ");
        }
        for (int j = 0; j < test; j++) {
            printf("*");
        }
        printf("\n");
    }
        return 0;
}