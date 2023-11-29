#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v={1,2,3,4,5,6};
    auto it=find(v.begin(),v.end(),3);
    if(it==v.end()) cout<<"not found";
    else cout<<"found";
    return 0;
}