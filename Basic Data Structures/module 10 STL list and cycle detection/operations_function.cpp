#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>mylist={2,4,6,1,5,1,3};
    // mylist.remove(1);
    // mylist.sort();
    // mylist.unique();
    mylist.reverse();
    for(int val:mylist)
    {
        cout<<val<<" ";
    }
    return 0;
}