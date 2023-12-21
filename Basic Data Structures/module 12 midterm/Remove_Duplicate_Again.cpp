#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
        int val;
        Node* next;
        Node* prev;
        Node(int val)
        {
            this->val=val;
            this->next=NULL;
            this->prev=NULL;
        }
};
void rmv_dplct(list<int>allnmbr)
{
    // allnmbr.sort();
    // allnmbr.unique(); 
    for(int val:allnmbr)
    {
        cout<<val<<" ";
    }
    
    
}
int main()
{
    list<int>allnmbr;
    int val;
    while(true)
    {
        cin>>val;
        if(val==-1)
        {
            break;
        }
        allnmbr.push_back(val);
    }
    allnmbr.sort();
    allnmbr.unique(); 
    rmv_dplct(allnmbr);
    return 0;
}