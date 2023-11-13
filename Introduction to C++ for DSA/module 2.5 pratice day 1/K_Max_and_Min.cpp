#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    if (a >= b && c >= b)
    {
        cout << b << " ";
    }
    else if (b >= a && c >= a)
    {
        cout << a << " ";
    }
    else
    {
        cout << c << " ";
    }
    if (a <= b && c <= b)
    {
        cout << b ;
    }
    else if (b <= a && c <= a)
    {
        cout << a ;
    }
    else
    {
        cout << c;
    }

    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K