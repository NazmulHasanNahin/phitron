#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        vector<int> A(N);
        int sum = 0;
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
            sum += A[i];
        }
        if (sum % 2 != 0)
        {
            cout << "NO" << endl;
            continue;
        }
        int half = sum / 2;
        vector<bool> dp(half + 1, false);
        dp[0] = true; //bs
        for (int i = 0; i < N; i++)
        {
            for (int j = half; j >= A[i]; j--)
            {
                if (dp[j - A[i]])
                {
                    dp[j] = true;
                }
            }
        }

        if (dp[half]==true)
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
