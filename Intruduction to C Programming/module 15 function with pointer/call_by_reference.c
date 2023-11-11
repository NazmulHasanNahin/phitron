#include<stdio.h>
void funct (int *p)
{
    *p=500;
}
int main()
{
    int x=100;
    funct(&x);
    printf("%p\n",&x);
    printf("%d\n",x);
    return 0;
}