#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    ll q;
    cin >> q;
    priority_queue<ll, vector<ll>, greater<ll>> arr;
    for (ll i = 0; i < q; i++)
    {
        ll type;
        cin >> type;
        if (type == 1)
        {
            ll a;
            cin >> a;
            arr.push(a);
        }
        else
        {
            if (arr.empty())
            {
                cout << "empty\n";
            }
            else
            {
                cout << arr.top() << "\n";
                ll min = arr.top();
                while (!arr.empty() && arr.top() == min)
                {
                    arr.pop();
                }
            }
        }
    }
    return 0;
}
