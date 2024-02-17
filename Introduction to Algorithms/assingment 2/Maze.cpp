#include <bits/stdc++.h>
using namespace std;
int dr[] = {0, 0, -1, 1};
int dc[] = {1, -1, 0, 0};
bool valid(int x, int y, int a, int b, vector<vector<char>> &maze, vector<vector<bool>> &visited)
{
    return x >= 0 && x < a && y >= 0 && y < b && maze[x][y] != '#' && !visited[x][y];
}
bool bfs(vector<vector<char>> &maze, pair<int, int> src, pair<int, int> dest, vector<vector<pair<int, int>>> &parent)
{
    int a = maze.size();
    int b = maze[0].size();
    vector<vector<bool>> visited(a, vector<bool>(b, false));
    queue<pair<int, int>> q;
    q.push(src);
    visited[src.first][src.second] = true;
    while (!q.empty())
    {
        pair<int, int> kot = q.front();
        q.pop();
        int x = kot.first;
        int y = kot.second;
        if (x == dest.first && y == dest.second)
        {
            return true;
        }
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dr[i];
            int ny = y + dc[i];
            if (valid(nx, ny, a, b, maze, visited))
            {
                visited[nx][ny] = true;
                parent[nx][ny] = {x, y};
                q.push({nx, ny});
            }
        }
    }
    return false;
}
void mark(vector<vector<char>> &maze, pair<int, int> dest, vector<vector<pair<int, int>>> &parent)
{
    pair<int, int> p = dest;
    while (maze[p.first][p.second] != 'R')
    {
        if (maze[p.first][p.second] != 'D') // trgt
        {
            maze[p.first][p.second] = 'X';
        }
        p = parent[p.first][p.second];
    }
}
int main()
{
    int a, b;
    cin >> a >> b;
    vector<vector<char>> maze(a, vector<char>(b));
    pair<int, int> src, dest;
    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            cin >> maze[i][j];
            if (maze[i][j] == 'R')
            {
                src = {i, j};
            }

            else if(maze[i][j] == 'D')
            {
                dest = {i, j};
            }
        }
    }
    vector<vector<pair<int, int>>> parent(a, vector<pair<int, int>>(b));
    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b;j++)
        {
            parent[i][j] = {i, j};
        }
    }
    if (bfs(maze, src, dest, parent))
    {
        mark(maze, dest, parent);
    }
    //lst
    for ( vector<char> row : maze)
    {
        for (char clm : row)
        {
            cout << clm;
        }   
        cout << endl;
    }
    return 0;
}