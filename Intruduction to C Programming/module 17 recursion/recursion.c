#include <stdio.h>
void fun()
{
    printf("fun");
    fun();
}           //cutation this  is a infinite loop

int main()
{
    fun();
    return 0;
}