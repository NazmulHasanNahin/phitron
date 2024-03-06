#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, h;
    cin >> n >> h;
    vector<int> monster(n);
    for (int i = 0; i < n; i++)
    {
        cin >> monster[i];
    }
    int max_health = monster[0];
    for (int i = 1; i < n; i++)
    {
        if (monster[i] > max_health)
        {
            max_health = monster[i];
        }
    }
    int moves = 0;
    while (true)
    {
        for (int i = 0; i < n; i++)
        {
            if (monster[i] > 0)
            {
                monster[i] = monster[i] - 1;
            }
        }
        moves++;
        bool all_dead = true;
        for (int i = 0; i < n; i++)
        {
            if (monster[i] > 0)
            {
                all_dead = false;
                break;
            }
        }
        if (all_dead)
        {
            cout << "Hablu" << endl;
            break;
        }
        int health = monster[0];
        for (int i = 1; i < n; i++)
        {
            if (monster[i] > health)
            {
                health = monster[i];
            }
        }
        h = h - health;
        moves++;
        if (h <= 0)
        {
            cout << "Dablu" << endl;
            break;
        }
    }
    return 0;
}
