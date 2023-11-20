#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string s;
        cin>>s;
        int sum1=s[0]-'0'+s[1]-'0'+s[2]-'0';
        int sum2=s[3]-'0'+s[4]-'0'+s[5]-'0';
        if (sum1==sum2)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
// https://codeforces.com/contest/1676/problem/A