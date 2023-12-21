#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>linkedlst;
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int pos,val;
        cin>>pos>>val;
        if(pos==0)
        {
            linkedlst.push_front(val);
        }
        else if(pos==1)
        {
            linkedlst.push_back(val);
        }
        else if(pos==2 && val<linkedlst.size())
        {
            int j=0;
            for(auto it=linkedlst.begin();it!=linkedlst.end();it++)
            {
                if(j==val)
                {
                    linkedlst.erase(it);
                    break;
                }
                j++;
            }
        }
        cout<<"L -> ";
        for(int value:linkedlst)
        {
            cout<<value<<" ";   //right
        }
        cout<<endl;
        linkedlst.reverse();
        cout<<"R -> ";
        for(int value:linkedlst)
        {
            cout<<value<<" ";   //ulta
        }
        cout<<endl;
        linkedlst.reverse();
    }
    return 0;
}