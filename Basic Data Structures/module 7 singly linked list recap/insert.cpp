#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
    }
};

void print_link_list(Node *head)
{
    Node *tmp = head;
    while (tmp!=NULL)
    {
        cout<<tmp->val<<" ";
        tmp=tmp->next;
    }
    cout<<endl;
}
void insert(Node* head,int pos,int val)
{
    Node* newNode=new Node(val);
    Node*tmp=head;
    for(int i=1;i<=pos-1;i++)
    {
        tmp=tmp->next;
    }
    // cout<<tmp->val<<" "; //confirm j temp position e ase

    newNode->next=tmp->next;
    tmp->next=newNode;
}
int size(Node*head)
{
    Node *tmp = head;
    int count=0;
    while (tmp!=NULL)
    {
        count++;
        tmp=tmp->next;
    }
    return count;
}
int main()
{
    Node *head = new Node(10);
    Node *a = new Node(20);
    Node *b = new Node(30);
    Node *c = new Node(40);
    Node *d = new Node(50);

    // a->next=b;
    // cout<<a->next->val;

    head->next = a;
    a->next = b;
    b->next = c;
    c->next = d;

    int pos,val;
    cin>>pos>>val;
    if(pos>size(head))
    {
        cout<<"Invalid Index";
    }
    else
    {
        insert(head,pos,val);
        print_link_list(head);
    }
    // insert(head,3,100);      //manual
    
    print_link_list(head);      // manual
    return 0;
}