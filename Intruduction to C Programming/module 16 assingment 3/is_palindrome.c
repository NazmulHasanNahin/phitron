#include <stdio.h>
#include <string.h>
int is_palindrome(char *x)
{
    int leanth = strlen(x);
    for (int i = 0; i < leanth / 2; i++)
    {
        if(x[i]!=x[leanth-1-i])
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    char strng[1000];
    scanf("%s", strng);
    int res=is_palindrome(strng);
    if(res==1)
    {
        printf("Palindrome\n");
    }
    else
    {
        printf("Not Palindrome\n");
    }
    return 0;
}