#include <bits/stdc++.h>
using namespace std;
int fact(int n)
{
    if (n == 0) // bs case
    {
        return 1;
    }
    int ft = fact(n - 1);
    return ft * n;
}
int main()
{
    int n;
    cin >> n;
    cout << fact(n);
    return 0;
}