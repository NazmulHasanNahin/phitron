#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,e;
    cin>>n>>e;
    vector<int> mat[n];

    for(int i=0;i<e;i++)
    {
        int a,b;
        cin>>a>>b;
        mat[a].push_back(b);
        mat[b].push_back(a);
    }
    for(int val:mat[0])
    {
        cout<<val<<" ";
    }
    return 0;
}