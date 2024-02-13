#include <bits/stdc++.h>
using namespace std;
const long long  N = 1e7;
vector<pair<long long, long long>> v[N];
long long dis[N];
class cmp
{
public:
    bool operator()(pair<long long, long long> a, pair<long long, long long> b)
    {
        return a.second > b.second;
    }
};
void dijkstra(int src)
{
    priority_queue<pair<long long, long long>, vector<pair<long long, long long>>, cmp> pq;
    pq.push({src, 0});
    dis[src] = 0;
    while (!pq.empty())
    {
        pair<long long, long long> parent = pq.top();
        pq.pop();
        long long node = parent.first;
        long long cost = parent.second;
        for (pair<long long, long long> child : v[node])
        {
            int childNode = child.first;
            int childCost = child.second;
            if (cost + childCost < dis[childNode])
            {
                dis[childNode] = cost + childCost;
                pq.push({childNode, dis[childNode]});
            }
        }
    }
}
int main()
{
    long long n, e;
    cin >> n >> e;
    while(e--)
    {
        long long a, b, c;
        cin >> a >> b >> c;
        v[a].push_back({b, c});
    }
    for (int i = 1; i <= n-1; i++)
    {
        dis[i] = 1e18;
    }
    long long src;
    cin >> src;
    dijkstra(src);
    long long t;
    cin >> t;
    while(t--)
    {
        long long destination;
        long long cost;
        cin >> destination >> cost;
        if (dis[destination] <= cost)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
