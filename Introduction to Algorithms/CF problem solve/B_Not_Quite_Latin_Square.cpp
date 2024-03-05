#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        vector<int> arr(3, 0);
        for (int i = 0; i < 9; i++)
        {
            char a;
            cin >> a;
            if (a == 'A')
            {
                arr[0]++;
            }
            if (a == 'B')
            {
                arr[1]++;
            }
            if (a == 'C')
            {
                arr[2]++;
            }
        }
        if (arr[0] == 2)
        {
            cout << "A" << endl;
        }
        if (arr[1] == 2)
        {
            cout << "B" << endl;
        }
        if (arr[2] == 2)
        {
            cout << "C" << endl;
        }
    }
    return 0;
}
// https://codeforces.com/contest/1915/problem/B