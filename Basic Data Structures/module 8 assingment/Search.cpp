#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
        int val;
        Node* next;
        Node(int val)
        {
            this->val=val;
            this->next=NULL;
        }
};
void insert_tail(Node *&head, Node *&tail, int val)
{
    Node *newNode = new Node(val);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
    }
    else
    {
        tail->next = newNode;
        tail = newNode;
    }
}
int indx(Node * head,int x)
{
    int cnt=0;
    Node* tmp=head;
    while(tmp!=NULL)
    {
        if(tmp->val==x)
        {
            return cnt;
        }
        tmp=tmp->next;
        cnt++;
    }
    return -1;
}
int main()
{
    int test;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        Node *head = NULL;
        Node *tail = NULL;
        int val;
        while (true)
        {
            cin >> val;
            if (val == -1)
            {
                break;
            }
            insert_tail(head, tail, val);
        }
        int x;
        cin>>x;
        int res=indx(head,x);
        cout<<res<<endl;
    }   
    return 0;
}