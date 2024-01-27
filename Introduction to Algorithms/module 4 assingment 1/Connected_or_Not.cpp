#include<bits/stdc++.h>
using namespace std;
const int N=1e+5;
vector<int>v[N];
int main()
{
    int n,e;
    cin>>n>>e;
    vector<vector<int>> mat(n,vector<int>(n,0));
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        v[a].push_back(b);
        mat[a][b] = 1;
    }
    int q;
    cin>>q;
    while(q--)
    {
        int a,b;
        cin>>a>>b;
        bool fnd=false;
        if (a == b || mat[a][b] == 1)
        {
            fnd=true;
        }
        else
        {
            for(int x:v[a])
            {
                if(x==b || a==b)
                {
                    fnd=true;
                    break;
                }
            }
        }
        if(fnd)
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
