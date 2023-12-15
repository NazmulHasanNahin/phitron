#include<bits/stdc++.h>
using namespace std;
int main()
{
    // list<int>mylist={10,20,40,50};
    // // list<int>mylist2={1,2,4,5};
    // list<int>newlist;
    // newlist=mylist;     //shortcut methode

    // newlist.assign(mylist.begin(),mylist.end());  //long methode
    // for(int val:newlist)
    // {
    //     cout<<val<<endl;
    // }





    list<int>mylist={10,20,30,40,50};

    // mylist.push_back(100);
    // mylist.push_front(100);
    // mylist.pop_back();
    // mylist.pop_back();
    // mylist.pop_front();

    // mylist.insert(next(mylist.begin(),2),100);
    // mylist.erase(next(mylist.begin(),2));

    // replace(mylist.begin(),mylist.end(),30,1783457);
    for(int val:mylist)
    {
        cout<<val<<" ";
    }
    return 0;
}