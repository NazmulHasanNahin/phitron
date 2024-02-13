#include <bits/stdc++.h>
using namespace std;
int dx[8] = {1, 1, -1, -1, 2, -2, 2, -2};
int dy[8] = {2, -2, 2, -2, 1, 1, -1, -1};
int minnmbr(int N, int M, pair<int, int> kn, pair<int, int> trgt)
{
    vector<vector<bool>> vis(N, vector<bool>(M, false));
    queue<pair<int, int>> q;
    q.push(kn);
    vis[kn.first][kn.second] = true;
    int ans = 0;
    while (!q.empty())
    {
        int sz = q.size();
        while (sz--)
        {
            pair<int, int> cur = q.front();
            q.pop();
            if (cur == trgt)
            {
                return ans;
            }
            for (int i = 0; i < 8; i++)
            {
                int x = cur.first + dx[i];
                int y = cur.second + dy[i];
                if (x >= 0 && x < N && y >= 0 && y < M && !vis[x][y])
                {
                    q.push({x, y});
                    vis[x][y] = true;
                }
            }
        }
        ans++;
    }
    return -1;
}
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        pair<int, int> kn, trgt;
        cin >> kn.first >> kn.second >> trgt.first >> trgt.second;
        int minn = minnmbr(N, M, kn, trgt);
        cout << minn << endl;
    }

    return 0;
}
