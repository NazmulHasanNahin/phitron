#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v={10,20,30,40,50};
    // v.erase(v.begin()+2);   //single value erase
    v.erase(v.begin()+1,v.begin()+4);
    for(int x:v)
    {
        cout<<x<<" ";
    }
    return 0;
}