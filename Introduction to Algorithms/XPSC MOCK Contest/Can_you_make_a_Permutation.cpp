#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while (T--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> v(n);
        vector<bool> x(n + 1, false);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
            if (v[i] <= n)
            {
                x[v[i]] = true;
            }
        }
        int changs = 0;
        for (int i = 1; i <= n; i++)
        {
            if (!x[i])
            {
                changs++;
            }
        }
        if (changs <= k)
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }
    }
    return 0;
}
