#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>mylist={10,20,30,40,50};
    // cout<<mylist.front()<<" ";
    // cout<<mylist.back()<<" ";
    cout<< *next(mylist.begin(),3)<<" ";
    return 0;
}