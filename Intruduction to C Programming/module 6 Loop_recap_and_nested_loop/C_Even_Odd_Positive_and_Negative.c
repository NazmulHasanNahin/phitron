/*Given N numbers. Count how many of these values are even, odd, positive and negative.

Input
First line contains one number N (1 ≤ N ≤ 103) number of values.

Second line contains N numbers (-105 ≤ Xi ≤ 105).

Output
Print four lines with the following format:

First Line: "Even: X", where X is the number of even numbers in the given input.

Second Line: "Odd: X", where X is the number of odd numbers in the given input.

Third Line: "Positive: X", where X is the number of positive numbers in the given input.

Fourth Line: "Negative: X", where X is the number of negative numbers in the given input.
link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/C
testing input:5
-5 0 -3 -4 12
*/
#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int a;
    int even=0,odd=0,pos=0,neg=0;
    for(int i=1;i<=n;i=i+1)
    {
        scanf("%d",&a);
        if(a%2==0)
        {
            even++;         //even 
        }
        else
        {
            odd++;      //odd   
        }
        if(a>0)
        {
            pos++;      //psoitive number 
        }
        else if(a<0)
        {
            neg++;      //negative number
        }
        
    }
    printf("Even: %d\nOdd: %d\nPositive: %d\nNegative: %d\n", even , odd , pos , neg);
    return 0;
}