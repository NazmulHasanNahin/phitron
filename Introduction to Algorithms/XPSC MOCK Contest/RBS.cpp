#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int sz;
        cin>>sz;
        vector<int>v(2,0);
        for(int i=0;i<sz;i++)
        {
            char a;
            cin>>a;
            if(a=='(')
            {
                v[0]++;
            }
            else if(a==')')
            {
                v[1]++;
            }
        }
        if(v[0]==v[1])
        {
            cout<<"Possible"<<endl;
        }
        else
        {
            cout<<"Impossible"<<endl;
        }
    }
    return 0;
}