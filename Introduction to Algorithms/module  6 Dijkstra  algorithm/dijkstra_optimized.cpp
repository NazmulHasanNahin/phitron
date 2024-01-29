#include <bits/stdc++.h>
using namespace std;
class cmp
{
    public:
    bool operator()(pair<int, int> a, pair<int, int> b)
    {
        return a.second>b.second;
    }
};
const int N = 100;
vector<pair<int, int>> v[N];
int dis[N];
void dijkstra(int src)
{
    queue<pair<int, int>> q;
    priority_queue<pair<int, int>,vector<pair<int, int>>,cmp> pq;
    pq.push({src, 0});
    dis[src] = 0;
    while (!pq.empty())
    {
        pair<int, int> parent = pq.top();
        pq.pop();
        int node = parent.first;
        int cost = parent.second;
        for (pair<int, int> child : v[node])
        {
            int childnode = child.first;
            int childcost = child.second;
            if (cost + childcost < dis[childnode])
            {
                // path relx
                dis[childnode] = cost + childcost;
                pq.push({childnode, dis[childnode]});
            }
        }
    }
}
int main()
{
    int n, e;
    cin >> n >> e;
    while (e--)
    {
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back({b, c});
        v[b].push_back({a, c});
    }
    for (int i = 0; i < n; i++)
    {
        dis[i]=INT_MAX;
    }
    dijkstra(0);
    for (int i = 0; i < n; i++)
    {
        cout << i << " -> " << dis[i] << endl;
    }
    return 0;
}