#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        int value;
        cin >> value;
        v.push_back(value);
    }
    int q;
    cin >> q;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int val : v)
    {
        pq.push(val);
    }
    for (int i = 0; i < q; i++)
    {
        int x;
        cin >> x;
        if (x == 0)
        {
            int value;
            cin >> value;
            pq.push(value);
            cout << pq.top() << endl;
        }
        else if (x == 1)
        {
            if (pq.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << pq.top() << endl;
            }
        }
        else if (x == 2)
        {
            if (pq.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                pq.pop();
                if (pq.empty())
                {
                    cout << "Empty" << endl;
                }
                else
                {
                    cout << pq.top() << endl;
                }
            }
            // if (pq.empty())
            // {
            //     cout << "Empty" << endl;
            // }
            // else
            // {
            //     cout << pq.top() << endl;
            // }
        }
    }
    return 0;
}