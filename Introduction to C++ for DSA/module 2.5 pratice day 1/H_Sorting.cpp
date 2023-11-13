#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++)
    {
        cin>>ar[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        int res=swap(ar[i],ar[j]);
        cout<<res;
    }
    return 0;
}