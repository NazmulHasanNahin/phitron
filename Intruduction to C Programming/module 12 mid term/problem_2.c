#include<stdio.h>
#include<string.h>
int main()
{
    char s[100001];
    scanf("%s",s);
    int leanth =strlen(s);
    int consonant=0;
    for(int i=0;i<leanth;i++)
    {
        char cnst =s[i];
        if(cnst != 'a' && cnst !='e' && cnst != 'i' && cnst != 'o' && cnst !='u')
        {
        consonant++;
        }
    }
    printf("%d\n",consonant);
    //printf("%s",s);
    return 0;
}