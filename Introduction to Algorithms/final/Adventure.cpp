#include <bits/stdc++.h>
using namespace std;
int knapsack(int n, int weight[], int val[], int W)
{
    if (n == 0 || W == 0)
    {
        return 0;
    }
    if (weight[n - 1] > W)
    {
        int op1 = knapsack(n - 1, weight, val, W);
        return op1;
    }
    else
    {
        int op1 = knapsack(n - 1, weight, val, W - weight[n - 1]) + val[n - 1];
        int op2 = knapsack(n - 1, weight, val, W);
        return max(op1, op2);
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, W;
        cin >> n >> W;
        int weight[n], val[n];
        for (int i = 0; i < n; i++)
        {
            cin >> weight[i];
        }
        for (int i = 0; i < n; i++)
        {
            cin >> val[i];
        }
        cout << knapsack(n, weight, val, W) << endl;
    }
    return 0;
}
