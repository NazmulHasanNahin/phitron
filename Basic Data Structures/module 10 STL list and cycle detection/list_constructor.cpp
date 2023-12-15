#include <bits/stdc++.h>
using namespace std;
int main()
{
    // list<int>mylist;
    // cout<<mylist.size();

    // list<int>mylist(10,5);
    // cout<<mylist.front();        //10 ta


    vector<int>v={10,20,30,50};
    // list<int> mylist(10,4);
    list<int>mylist(v.begin(),v.end());
    // for (auto it =mylist.begin();it != mylist.end();it++)
    // {
    //     cout<<*it<<endl;     //1st methode
    // }


    for(int val:mylist)
    {
        cout<<val<<endl;        //2nd methode
    }
    return 0;
}