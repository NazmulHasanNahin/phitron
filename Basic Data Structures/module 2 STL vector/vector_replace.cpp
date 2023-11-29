#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v={1,2,3,4,2,5,6};
    replace(v.begin(),v.end(),2,3999);
    for(int x:v)
    {
        cout<<x<<" ";
    }
    return 0;
}