#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        string s;
        cin>>n;
        cin>>s;
        int ans=1;
        for(int i=0;i<n;i++)
        {
            ans=max(ans,s[i]-'a'+1);
        }
        cout<<ans<<'\n';
    }
    return 0;
}
// https://codeforces.com/contest/1760/problem/B