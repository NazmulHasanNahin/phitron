#include <stdio.h>
void func(int a, int b, int c)
{
    int temp;
    if (a > b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    if (b > c)
    {
        temp = b;
        b = c;
        c = temp;
    }
    if (a > b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    printf("%d\n%d\n%d\n", a, b, c);
}
int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    func(a, b, c);
    printf("\n");
    printf("%d\n%d\n%d\n", a, b, c);
    return 0;
}