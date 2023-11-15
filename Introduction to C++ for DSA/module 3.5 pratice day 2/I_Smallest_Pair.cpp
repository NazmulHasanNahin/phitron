#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int T = 0; T < t; ++T)
    {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
        }
        long long result = LLONG_MAX;
        // Print the smallest possible result of Ai + Aj + j - i , where 1  ≤  i < j  ≤  N.
        for (int i = 0; i < n; ++i)
        {
            for (int j = i+1; j < n; ++j)
            {
                result = min(result,(long long)(a[i] + a[j] + j - i));
            }
        }
        cout<<result<<endl;
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I