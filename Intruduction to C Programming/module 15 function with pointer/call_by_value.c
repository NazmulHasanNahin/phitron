#include<stdio.h>
void fun(int x)
{
    // printf("fun x eer adress %p\n",&x);
    x=200;
    printf("fun x e r vlaue %d\n",x);
}
int main()
{
    int x=10;
    // printf("main x eer adress %p\n",&x);
    fun(x);
    printf("main x e r vlaue %d\n",x);
    return 0;
}