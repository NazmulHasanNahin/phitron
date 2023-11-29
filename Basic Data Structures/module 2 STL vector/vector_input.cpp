#include<bits/stdc++.h>
using namespace std;
int main()
{
    // vector<int>v;
    // int n;
    // cin>>n;
    // for(int i=0;i<n;i++)
    // {
    //     int x;
    //     cin>>x;                  //1st type
    //     v.push_back(x);
    // }
    // for(int value:v)
    // {
    //     cout<<value<<" ";
    // }


    int n;
    cin>>n;
    vector<int>v(n);
    for(int i=0;i<n;i++)
    {
        cin>>v[i];
    }
    for(int i=0;i<n;i++)            //2nd type // easy
    {
        cout<<v[i]<<endl;
    }
    return 0;
}