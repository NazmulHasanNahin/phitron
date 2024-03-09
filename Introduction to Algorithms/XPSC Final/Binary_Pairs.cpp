#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        string ss;
        cin >> ss;
        int cnt = 0;
        for (int i = 0; i < n - 1; i++)
        {
            if (ss[i] == '0' && ss[i + 1] == '1')
            {
                cnt++;
            }
            else if (ss[i] == '1' && ss[i + 1] == '0')
            {
                cnt++;
            }
        }
        cout << cnt << endl;
    }
    return 0;
}
