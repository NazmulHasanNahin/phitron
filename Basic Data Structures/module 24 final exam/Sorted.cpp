#include <bits/stdc++.h>
using namespace std;

void rmv_duplicate_print(vector<int> v)
{
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    for (int val : v)
    {
        cout << val << " ";
    }
    cout << endl;
}

int main()
{
    int test;
    cin>>test;
    for (int t = 0; t < test; t++)
    {
        int n;
        cin>>n;
        vector<int>v;
        for(int i=0;i<n;i++)
        {
            int a;
            cin>>a;
            v.push_back(a);
        }
        rmv_duplicate_print(v);
    }
    return 0;
}