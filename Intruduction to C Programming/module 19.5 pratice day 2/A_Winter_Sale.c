#include<stdio.h>
int main()
{
    int x;
    float p;
    scanf("%d %f",&x,&p);
    //printf("%d %d",x,p);
    float orginal_price=(p/(1-x/100.0));
    printf("%0.2f",orginal_price);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/A