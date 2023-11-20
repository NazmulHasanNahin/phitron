#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int test = 0; test < t; test++)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<int> lst(26, -1);
        int balloons = 0;
        for (int i = 0; i < n; i++)
        {
            int x = s[i] - 'A';
            if (lst[x] == -1)
            {              
                balloons += 2;
            }
            else
            {               
                balloons += 1;
            }
            lst[x] = i;
        }
        cout << balloons << endl;
    }
    return 0;
}
// https://codeforces.com/contest/1703/problem/B