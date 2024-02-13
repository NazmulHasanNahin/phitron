#include <bits/stdc++.h>
#define ll long long int
using namespace std;
const long long int INF = 1e18;
int main()
{
    ll N, E;
    cin >> N >> E;
    ll graph[N+1][N+1];
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            graph[i][j] = 1e18;
            if (i == j)
                graph[i][j] = 0;
        }
    }
    for (ll i = 0; i < E; i++)
    {
        ll u, v, w;
        cin >> u >> v >> w;
        graph[u][v] = min(graph[u][v], w);
    }
    // for (ll k = 1; k <= N; k++)
    // {
    //     for (ll i = 1; i <= N; i++)
    //     {
    //         for (ll j = 1; j <= N; j++)
    //         {
    //             if (graph[i][k] != INF && graph[k][j] != INF)
    //             {
    //                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
    //             }
    //         }
    //     }
    // }
    for (int k = 1; k <= N; k++)
    {
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                if (graph[i][k] + graph[k][j] < graph[i][j])
                {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }
    ll q;
    cin >> q;
    while (q--)
    {
        ll src, dest;
        cin >> src >> dest;
        if (graph[src][dest] == INF)
        {
            cout << -1 << endl;
        }
        else
        {
            cout << graph[src][dest] << endl;
        }
    }
    return 0;
}
