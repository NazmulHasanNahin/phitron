#include<stdio.h>
 // return_type(parameter)
    // {
    //     code
    //     return watttt?   //this is the syntax of function
    // }

int sum(int x,int y)
{
    //code
    int sum=x+y;
    return sum;
}
int main()
{
   int s=sum(100,20);
   printf("%d",s);

    return 0;
}