#include<stdio.h>
int main()
{
    int ar[10000];
    int size=sizeof(ar)/sizeof(int);
    printf("%d",size);
    //printf("%d",sizeof(ar));
    return 0;
}