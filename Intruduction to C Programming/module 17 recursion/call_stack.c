#include<stdio.h>
void world()
{
    printf("world\n");
}
void hello()
{
    printf("hello\n");
    world();
}
int main()
{
    hello();
    printf("end\n");
    return 0;
}