#include<stdio.h>
int my_abs(int n)
{
    if(n<0)
    {
        printf("%d",(n*(-1)));
    }
    else
    {
        printf("%d",n);
    }
    return n;
}
int main()
{
    int n;
    scanf("%d",&n);
    my_abs(n);
    return 0;
}
// https://docs.google.com/document/d/1xhF5KOCzEu-6HGqsW6X1BFTUpIUekQCZ/edit