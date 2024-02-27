#include<bits/stdc++.h>
using namespace std;
bool perfectscore(int N, int M,vector<int> &marks)
{
    int target = 1000 - M;
    if (target < 0)
    {
        return false;
    }
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    for (int mark : marks)
    {
        for (int j = target;j >= mark; j--)
        {
            if (dp[j - mark])
            {
                dp[j] = true;
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
        int N, M;
        cin >> N >> M;
        vector<int> marks(N);
        for (int i = 0; i < N; i++)
        {
            cin >> marks[i];
        }
        if (perfectscore(N, M, marks))
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