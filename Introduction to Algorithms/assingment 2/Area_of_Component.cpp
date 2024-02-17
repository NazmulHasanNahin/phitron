#include <bits/stdc++.h>
using namespace std;
const int N=1e3;
char a[N][N];
bool vis[N][N];
vector<pair<int, int>> d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
int n, m;
int area;
bool valid(int i, int j)
{
    if (i < 0 || i >= n || j < 0 || j >= m || a[i][j] == '-')
        return false;
    return true;
}
void dfs(int si, int sj)
{
    vis[si][sj] = true;
    area++;
    for (int i = 0; i < 4; i++)
    {
        int ci = si + d[i].first;
        int cj = sj + d[i].second;
        if (valid(ci, cj) && !vis[ci][cj])
        {
            dfs(ci, cj);
        }
    }
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
        }
    }
    int min_area = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] == '.' && !vis[i][j])
            {
                area = 0;
                dfs(i, j);
                min_area = min(min_area, area);
            }
        }
    }
    if (min_area == INT_MAX)
    {
        cout << "-1" << endl;
    }
    else
    {
        cout << min_area << endl;
    }
    return 0;
}
