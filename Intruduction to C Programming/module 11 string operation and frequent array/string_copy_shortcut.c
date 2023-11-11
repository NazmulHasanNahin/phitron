#include<stdio.h>
#include<string.h>
int main()
{
    char a[100],b[100];
    scanf("%s %s",a,b);
    strcpy(b,a);            // a,b value chjab=nge kore dilei print change hoe jabe
    printf("%s %s",a,b);
    return 0;
}