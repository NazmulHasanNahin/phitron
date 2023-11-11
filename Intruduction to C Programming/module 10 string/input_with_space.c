#include<stdio.h>
#include<string.h>
int main()
{
    char a[19];
    fgets(a,12,stdin);
    printf("%s",a);
    return 0;
}
