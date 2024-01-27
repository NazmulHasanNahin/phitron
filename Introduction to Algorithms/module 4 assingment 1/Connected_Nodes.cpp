#include<bits/stdc++.h>
using namespace std;
const int N=1e+5;
int main()
{
    int n,e;
    cin>>n>>e;
    vector<int>v[n];
    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
    {
        int x;
        cin>>x;
        vector<int> node=v[x];
        if(node.empty())
        {
            cout<<-1<<endl;
        }
        else
        {
            sort(node.begin(),node.end(),greater<int>());
            for(int c:node)
            {
                cout<<c<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}