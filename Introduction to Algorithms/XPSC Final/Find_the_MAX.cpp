#include<bits/stdc++.h>
#define ll long long
using namespace std;
class cmp
{
    public:
    bool operator()(pair<ll, ll> a,pair<ll, ll> b) 
    {
        if (a.second == b.second)
        {
            return a.first < b.first;
        }
        return a.second < b.second;
    }
};
int main()
{
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, cmp> pq;
    unordered_map<ll, ll> frq;
    ll q;
    cin >> q;
    while (q--)
    {
        ll type;
        cin >> type;
        if (type == 1)
        {
            ll c;
            cin >> c;
            frq[c]++;
            pq.push({c, frq[c]});
        }
        else
        {
            if (pq.empty())
            {
                cout << "empty\n";
            }
            else
            {
                while (!pq.empty() && frq[pq.top().first] != pq.top().second)
                {
                    pq.pop();
                }
                if (!pq.empty())
                {
                    pair<ll, ll> top = pq.top();
                    cout << top.first << "\n";
                    frq[top.first] = 0;
                    pq.pop();
                }
                else
                {
                    cout << "empty\n";
                }
            }
        }
    }

    return 0;
}
