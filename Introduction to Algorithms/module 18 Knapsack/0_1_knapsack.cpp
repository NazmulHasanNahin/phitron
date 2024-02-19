#include <bits/stdc++.h>
using namespace std;
int knapsack(int n, int weight[], int value[], int w)
{
    if(n<0 || w==0)
    {
        return 0;
    }
    if (weight[n] <= w)
    {
        int op1 = knapsack(n - 1, weight, value, w - weight[n]) + value[n];
        int op2 = knapsack(n - 1, weight, value, w);
        return max(op1,op2);
    }
    else
    {
        int op2 = knapsack(n - 1, weight, value, w);
        return op2;
    }
}
int main()
{
    int n;
    cin >> n;
    int weight[n], value[n];
    for (int i = 0; i < n; i++)
    {
        cin >> weight[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> value[i];
    }
    int w;
    cin >> w;
    cout << knapsack(n - 1, weight, value, w) << endl;
    return 0;
}