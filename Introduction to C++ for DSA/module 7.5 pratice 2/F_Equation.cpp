#include <bits/stdc++.h>
using namespace std;
long long sum(long long int n, long long int m)
{
    double sum = 0;
    for (long long int i = 2; i <= m; i += 2)
    {
        sum += pow(n*1.0, i*1.0);
    }
    return sum;
}

int main()
{
    long long int n, m;
    cin >> n >> m;
    cout << sum(n,m) << endl;
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F