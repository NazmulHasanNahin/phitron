#include <stdio.h>
int main()
{
    int testcase;
    scanf("%d", &testcase);
    for (int t = 0; t < testcase; t++)
    {
        int N;
        scanf("%d", &N);
        int x;
        int A[N];
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &A[i]);
        }
        scanf("%d", &x);
        for (int i = 0; i < N; i++)
        {
            if (A[i] == x)
            {
                printf("YES\n");
                break;
            }
            else if(i == N - 1)
            {
                printf("NO\n");
                break;
            }
        }
    }
    return 0;
}