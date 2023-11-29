#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v={1,2,3,4};
    vector<int>v1={10,20,30};
    v.insert(v.begin()+2,v1.begin(),v1.end());
    for(int x:v)
    {
        cout<<x<<" ";
    }
    return 0;
}