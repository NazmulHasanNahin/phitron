#include<stdio.h>
int my_len(char str[])
{
    int count=0;
    for(count=0;str[count]!='\0';count++)
    {
    }
    return count;
}
int main()
{
    char inp_str[100];
    scanf("%s",inp_str);
    int charlen=my_len(inp_str);
    printf("%d",charlen);
    return 0;
}