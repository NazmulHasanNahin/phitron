#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int mx;
    cin >> mx;
    for (int i = 1; i < n; i++)
    {
        int num;
        cin >> num;
        mx = max(mx, num);
    }

    cout << mx << endl;
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/E