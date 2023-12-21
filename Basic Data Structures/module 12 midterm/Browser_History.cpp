#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
        string val;
        Node* next;
        Node* prev;
        Node(string val)
        {
            this->val=val;
            this->next=NULL;
            this->prev=NULL;
        }
};
void insert_at_tail(Node* &head,Node* &tail,string val)
{
    Node* newNode=new Node(val);
    if(tail==NULL)
    {
        head=newNode;
        tail=newNode;
        return;
    }
    tail->next=newNode;
    newNode->prev=tail;
    tail=newNode;
}
void print_(string val)
{
    cout<<val<<endl;
}
int main()
{
    Node* head=NULL;
    Node* tail=NULL;
    string val;
    while(true)
    {
        cin>>val;
        if(val=="end")
        {
            break;
        }
        insert_at_tail(head,tail,val);
    }
    Node* cur=head;
    int t;
    cin>>t;
    for(int test=0;test<t;test++)
    {
        string cmd,site;
        cin>>cmd;
        if(cmd=="visit")
        {
            cin>>site;
            Node* tmp=head;
            bool found=false;
            while(tmp!=NULL)
            {
                if(tmp->val==site)
                {
                    found=true;
                    break;
                }
                tmp=tmp->next;
            }
            if(found==true)
            {
                print_(site);
                cur=tmp;
            }
            else
            {
                cout<<"Not Available"<<endl;
            }
        }
        else if(cmd=="next")
        {
            if(cur!=NULL && cur->next!=NULL)
            {
                cur=cur->next;
                print_(cur->val);
            }
            else
            {
                cout<<"Not Available"<<endl;
            }
        }
        else if(cmd=="prev")
        {
            if(cur!=NULL && cur->prev!=NULL)
            {
                cur=cur->prev;
                print_(cur->val);
            }
            else
            {
                cout<<"Not Available"<<endl;
            }
        }
    }
    return 0;
}