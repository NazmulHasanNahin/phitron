#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
int par[N];
int grp_size[N];
void dsu_initalize(int n)
{
    for (int i = 0; i < n; i++)
    {
        par[i] = i;
        grp_size[i] = 1;
    }
}
int dsu_find(int node)
{
    if (par[node] == node)
        return node;
    return par[node] = dsu_find(par[node]);
}
void dsu_union(int node1, int node2)
{
    int leaderA = dsu_find(node1);
    int leaderB = dsu_find(node2);
    if (leaderA != leaderB)
    {
        par[leaderA] = leaderB;
        grp_size[leaderB] += grp_size[leaderA];
    }
}
int main()
{
    int n, m;
    cin >> n >> m;
    dsu_initalize(n);
    vector<pair<int, int>> edges;
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }
    int cycle = 0;
    for (pair<int, int> edge : edges)
    {
        int u = edge.first;
        int v = edge.second;
        int leaderU = dsu_find(u);
        int leaderV = dsu_find(v);
        if (leaderU == leaderV)
        {
            cycle++;
        }
        else
        {
            dsu_union(u, v);
        }
    }
    cout << cycle << endl;
    return 0;
}
