#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int test = 0; test < t; test++)
    {
        string s, x;
        cin >> s >> x;
        int idx=s.find(x);
        // cout<<idx;
        while(idx!=-1)
        {
           s.replace(idx,x.length(),"#"); 
            idx=s.find(x,idx+1);
        }
        cout<<s<<endl; 
    }
    return 0;
}