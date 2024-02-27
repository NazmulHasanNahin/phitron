#include <bits/stdc++.h>
using namespace std;
bool final(int target)
{
    vector<bool> dp(target + 1, false);
    dp[1] = true;
    for (int i = 1; i <= target; ++i)
    {
        if (dp[i])
        {
            if (i + 3 <= target)
            {
                dp[i + 3] = true;
            }
            if (i * 2 <= target)
            {
                dp[i * 2] = true;
            }
        }
    }
    return dp[target];
}
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        if (final(n))
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
