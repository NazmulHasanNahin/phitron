#include<bits/stdc++.h>
using namespace std;
const int N=1000;
char a[N][N];
bool vis[N][N];
int n,m;
vector<pair<int, int>> v = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
bool valid(int ci,int cj)
{
    return (ci>=0 && ci<n && cj>=0 && cj<m);
}
void dfs(int si,int sj)
{
    vis[si][sj]=true;
    for(int i=0;i<m;i++)
    {
        int xi=si+v[i].first;
        int xj=sj+v[i].second;
        if(valid(xi,xj) && a[xi][xj] =='.' && !vis[xi][xj])
        {
            dfs(xi,xj);
        }
    }
}
int main()
{
    cin>>n>>m;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>a[i][j];
        }
    }
    int si,sj;
    cin>>si>>sj;
    int x,y;
    cin>>x>>y;
    dfs(si,sj);
    if(vis[x][y])
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    return 0;
}