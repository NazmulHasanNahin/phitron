#include<bits/stdc++.h>
using namespace std;
pair<long long, long long> mxwater(vector<long long> height)
{
    long long max1 = 0, max2 = -1;
    for (long long i = 1; i < height.size(); i++)
    {
        if (height[i] > height[max1])
        {
            max2 = max1;
            max1 = i;
        }
        else if (max2 == -1 || height[i] > height[max2])
        {
            max2 = i;
        }
    }
    if (max1 > max2)
    {
        swap(max1, max2);
    }
    return make_pair(max1, max2);
}
int main()
{
    long long T;
    cin >> T;
    while (T--)
    {
        long long n;
        cin >> n;
        vector<long long> height(n);
        for (long long i = 0; i < n; i++)
        {
            cin >> height[i];
        }
        pair<long long, long long> out = mxwater(height);
        cout << out.first << " " << out.second << endl;
    }

    return 0;
}
