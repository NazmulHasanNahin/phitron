#include <stdio.h>
int main()
{
    int x = 100;
    int *ptr = &x;
    // printf("x %p\n",&x);
    // printf("ptr %p\n",ptr);
    // int x=200;
    printf(" x er value %d\n", x);
    printf(" x er value %d", *ptr);
    return 0;
}