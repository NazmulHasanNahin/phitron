#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int ar[n];
    for (int i = 0; i < n; i++)
    {
        cin >> ar[i];
    }
    // sort(ar,ar+n);   \\acending order    choto theke boro
    sort(ar,ar+n,greater<int>());   //decending order       boro theke choto
    for (int i = 0; i < n; i++)
    {
        cout << ar[i] << " ";
    }
    return 0;
}