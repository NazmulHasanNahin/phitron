#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++)
    {
        char S[10001];
        scanf("%s", S);
        // printf("%s",S);
        int capital= 0;
        int small = 0;
        int digit= 0;
        for (int i= 0; S[i] != '\0';i++)
        {
            if (S[i] >= 'A' && S[i] <= 'Z')
            {
                capital++;
            }
            else if (S[i] >= 'a' && S[i] <= 'z')
            {
                small++;
            }
            else if (S[i] >='0' && S[i] <= '9')
            {
                digit++;
            }
        }
        printf("%d %d %d\n", capital, small, digit);
    }
    return 0;
}
