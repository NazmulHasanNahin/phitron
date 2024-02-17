#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 5;
long long parent[N];
long long sz[N];
class Edge
{
public:
    long long src, dest, weight;
    Edge(long long src, long long dest, long long weight)
    {
        this->src = src;
        this->dest = dest;
        this->weight = weight;
    }
};
bool cmp(Edge a, Edge b)
{
    return a.weight < b.weight;
}
void initialze(long long n)
{
    for (long long i = 1; i <= n; i++)
    {
        parent[i] = i;
        sz[i] = 1;
    }
}
int dsu_find(long long v)
{
    if (v == parent[v])
    {
        return v;
    }
    long long leader = dsu_find(parent[v]);
    parent[v] = leader;
    return leader;
}
void union_s(long long a, long long b)
{
    a = dsu_find(a);
    b = dsu_find(b);
    if (a != b)
    {
        if (sz[a] < sz[b])
        {
            swap(a, b);
        }
        parent[b] = a;
        sz[a] += sz[b];
    }
}
int main()
{
    long long n, m;
    cin >> n >> m;
    vector<Edge> edges;
    for (long long i = 0; i < m; ++i)
    {
        long long src, dest, weight;
        cin >> src >> dest >> weight;
        edges.push_back(Edge(src, dest, weight));
    }
    sort(edges.begin(), edges.end(), cmp);
    initialze(n);
    long long cost = 0;
    long long remove_road = 0;
    for (Edge x : edges)
    {
        long long u = dsu_find(x.src);
        long long v = dsu_find(x.dest);

        if (u != v)
        {
            cost += x.weight;
            union_s(u, v);
        }
        else
        {
            remove_road++;
        }
    }
    for (long long i = 2; i <= n; ++i)
    {
        if (dsu_find(i) != dsu_find(1))
        {
            cout << "Not Possible"<<endl;
            return 0;
        }
    }
    cout << remove_road << " " << cost <<endl;
    return 0;
}