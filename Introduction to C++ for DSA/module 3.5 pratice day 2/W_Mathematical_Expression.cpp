#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a, b;
    char q;
    char s;
    int result;
    cin >> a >> s >> b >> q >> result;
    if (s == '+')
    {
        if (a + b == result)
        {
            cout << "Yes";
            //     return 0;
        }
        else
        {
            cout << (a + b);
        }
    }
    else if (s == '-')
    {
        if (a - b == result)
        {
            cout << "Yes";
            return 0;
        }
        else
        {
            cout << (a - b);
        }
    }
    else if (s == '*')
    {
        if (a * b == result)
        {
            cout << "Yes";
        }
        else
        {
            cout << (a * b);
        }
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/W