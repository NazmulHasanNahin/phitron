#include<bits/stdc++.h>
using namespace std;
int main()
{
    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    int max_even = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        if (arr[i] % 2 == 0)
        {
            max_even = arr[i];
            break;
        }
    }
    if ((arr[N - 1] + arr[N - 2]) % 2 == 0)
    {
        max_even = max(max_even, arr[N - 1] + arr[N - 2]);
    }
    else
    {
        for (int i = 0; i < N - 1; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                if ((arr[i] + arr[j]) % 2 == 0)
                {
                    max_even = max(max_even, arr[i] + arr[j]);
                }
            }
        }
    }
    cout << max_even << endl;
    return 0;
}
