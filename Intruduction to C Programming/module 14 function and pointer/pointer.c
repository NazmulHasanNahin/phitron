// #include<stdio.h>
// int main()
// {
//     int x=100;
//     printf("%p\n",&x);
//     int *p= &x;
//     printf("%p\n",p);
//     return 0;
// }
#include <stdio.h>
int sum(int x, int y)
{
    int res = x + y;
    return res;
}
int main()
{
    sum(5, 6);
    return 0;
}