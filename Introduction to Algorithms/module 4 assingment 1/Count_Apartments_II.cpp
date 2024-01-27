#include <bits/stdc++.h>
using namespace std;
int n, m;
const int N = 1001;
char a[N][N];
vector<pair<int, int>> v = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
bool valid(int i, int j)
{
    return (i >= 0 && i < n && j >= 0 && j < m && a[i][j] == '.');
}
int dfs(int i, int j)
{
    a[i][j] = '#';
    int room = 1;
    for (pair<int, int> p : v)
    {
        int dx = p.first;
        int dy = p.second;
        if (valid(i + dx, j + dy))
        {
            room += dfs(i + dx, j + dy);
        }
    }
    return room;
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
    vector<int> count;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (a[i][j] == '.')
            {
                count.push_back(dfs(i, j));
            }
        }
    }
    if (count.empty())
    {
        cout << 0 << endl;
    }
    else
    {
        sort(count.begin(), count.end());
        for (int x : count)
        {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}