#include <bits/stdc++.h>
int getsum(stack<int>s)
{
    int sum=0;
    while(!s.empty())
    {
        sum=sum+s.top();
        s.pop();
    }
    return sum;
}
int maxSum(stack<int> &s1, stack<int> &s2, stack<int> &s3) 
{
    int sum1=getsum(s1);
    int sum2=getsum(s2);
    int sum3=getsum(s3);
    cout<<sum1<<" "<<sum2<<" "<<sum3<<" ";
}
// https://www.codingninjas.com/studio/problems/maximum-equal-stack-sum_1062571