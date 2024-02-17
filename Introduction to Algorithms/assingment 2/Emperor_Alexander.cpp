#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 5;
long long parent[N];
long long group_size[N];
void dsu_initialize(long long n)
{
    for (long long i = 0; i < n; i++)
    {
        parent[i] = -1;
        group_size[i] = 1;
    }
}
long long dsu_find(long long node)
{
    if (parent[node] == -1)
        return node;
    long long leader = dsu_find(parent[node]);
    parent[node] = leader;
    return leader;
}
void dsu_union_by_size(long long node1, long long node2)
{
    long long leaderA = dsu_find(node1);
    long long leaderB = dsu_find(node2);
    if (group_size[leaderA] > group_size[leaderB])
    {
        parent[leaderB] = leaderA;
        group_size[leaderA] += group_size[leaderB];
    }
    else
    {
        parent[leaderA] = leaderB;
        group_size[leaderB] += group_size[leaderA];
    }
}
class Edge
{
public:
    long long u, v, w;
    Edge(long long u, long long v, long long w)
    {
        this->u = u;
        this->v = v;
        this->w = w;
    }
};
bool cmp(Edge a, Edge b)
{
    return a.w < b.w;
}
int main()
{
    long long n, e;
    cin >> n >> e;
    dsu_initialize(n);
    vector<Edge> edgelist;
    while (e--)
    {
        long long u, v, w;
        cin >> u >> v >> w;
        edgelist.push_back(Edge(u, v, w));
    }
    sort(edgelist.begin(), edgelist.end(), cmp);
    long long tcost = 0;
    long long roadsRemoved = 0;
    for (Edge ed : edgelist)
    {
        long long leaderU = dsu_find(ed.u);
        long long leaderV = dsu_find(ed.v);
        if (leaderU == leaderV)
        {
            roadsRemoved++;
            if (roadsRemoved == n - 1)
            {
                cout << roadsRemoved << " " << tcost << endl;
                return 0;
            }
            continue;
        }
        else
        {
            dsu_union_by_size(ed.u, ed.v);
            tcost += ed.w;
        }
    }
    cout << "Not Possible" << endl;
    return 0;
}
