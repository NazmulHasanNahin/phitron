#include <bits/stdc++.h>
using namespace std;
const long long N = 1e5 + 5;
const long long mx = 1e18+5;
class Edge
{
public:
    long long u, v;
    long long c;
    Edge(long long u, long long v, long long c)
    {
        this->u = u;
        this->v = v;
        this->c = c;
    }
};
int main()
{
    long long n, e;
    cin >> n >> e;
    vector<Edge> Edgelist;
    while (e--)
    {
        long long u, v;
        long long c;
        cin >> u >> v >> c;
        Edgelist.push_back(Edge(u, v, c));
    }
    vector<long long> dis(N, mx);
    long long src;
    cin >> src;
    src--;
    dis[src] = 0;
    for (int i = 1; i <= n - 1; i++)
    {
        for (Edge ed : Edgelist)
        {
            long long u = ed.u - 1;
            long long v = ed.v - 1;
            long long c = ed.c;
            if (dis[u] < mx && dis[u] + c < dis[v])
            {
                dis[v] = dis[u] + c;
            }
        }
    }
    bool negative_cycle = false;
    for (Edge ed : Edgelist)
    {
        long long u = ed.u - 1;
        long long v = ed.v - 1;
        long long c = ed.c;
        if (dis[u] < mx && dis[u] + c < dis[v])
        {
            negative_cycle = true;
            break;
        }
    }
    if (negative_cycle)
    {
        cout << "Negative Cycle Detected" << endl;
    }
    else
    {
        int T;
        cin>>T;
        for (int i = 0; i < T; i++)
        {
            long long dest;
            cin>>dest;
            if (dis[dest - 1] == mx)
            {
                cout << "Not Possible" << endl;
            }
            else
            {
                cout << dis[dest - 1] << endl;
            }
        }
    }
    return 0;
}
