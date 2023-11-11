#include<stdio.h>
int main()
{
    double  x=5.26;
    double * ptr=&x;
    *ptr=10.20;                         
    printf("x er adress %0.3lf\n3",x);
    printf("ptr er adress %0.3lf\n",*ptr);
    printf("ptr er size %d",sizeof(ptr));
    return 0;
}