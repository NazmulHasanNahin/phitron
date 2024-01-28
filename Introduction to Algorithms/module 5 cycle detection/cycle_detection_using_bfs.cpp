#include<bits/stdc++.h>
using namespace std;
const int N=1e5+5;
bool vis[N];
vector<int> adj[N];
int parentarry[N];
bool ans;
void bfs(int s)
{
    queue<int>q;
    q.push(s);
    vis[s]=true;
    while(!q.empty())
    {
        int parent =q.front();
        
        q.pop();
        for(int child:adj[parent])
        {
            if(vis[child] && parentarry[parent]!=child)
            {
                ans=true;
            }
            if(!vis[child])
            {
                vis[child]=true;
                parentarry[child]=parent;
                q.push(child);

            }
        }
    }
}
int main()
{
    int n,e;
    cin>>n>>e;
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        adj[a].push_back(b);
        adj[b].push_back(a);

    }
    memset(vis,false,sizeof(vis));
    memset(parentarry,-1,sizeof(parentarry));
    ans=false;
    for(int i=0;i<n;i++)
    {
        if(!vis[i])
        {
            bfs(i);
        }
    }
    if(ans) cout<<"Cycle ase";
    cout<<"nai";
    return 0;
}