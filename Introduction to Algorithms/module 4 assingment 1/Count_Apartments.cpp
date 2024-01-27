#include <bits/stdc++.h>
using namespace std;
const int N = 1001;
char a[N][N];
int n, m;
vector<pair<int, int>> v = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
bool valid(int i, int j)
{
    return (i >= 0 && i < n && j >= 0 && j < m && a[i][j] == '.');
}
void dfs(int i, int j)
{
    a[i][j] = '#';
    for (pair<int, int> p : v)
    {
        int dx = p.first;
        int dy = p.second;
        if (valid(i + dx, j + dy))
        {
            dfs(i + dx, j + dy);
        }
    }
}
int totalaprt()
{
    int number=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(a[i][j]=='.')
            {
                number++;
                dfs(i,j);
            }
        }
    }
    return number;
}
int main()
{
    cin>>n>>m;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>a[i][j];
        }
    }
    int res=totalaprt();
    cout<<res<<endl;
    return 0;
}