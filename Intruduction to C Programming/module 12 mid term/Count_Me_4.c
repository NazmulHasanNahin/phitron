#include <stdio.h>
int main()
{
    char a;
    int count[26] = {0};
    while (scanf("%c", &a) != EOF)
    {
        count[a - 'a']++;
    }
    for (char i = 'a'; i <= 'z'; i++)
    {
        if (count[i - 'a'] > 0)
        {
            printf("%c - %d\n", i, count[i - 'a']);
        }
    }
    return 0;
}
