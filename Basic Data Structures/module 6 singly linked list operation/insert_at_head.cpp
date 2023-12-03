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
void insert_at_tail(Node *&head, int v)
{
    Node *newNode = new Node(v);
    if (head == NULL)
    {
        head = newNode;
        cout << "insterted at head" << endl
        << endl;
        return;
    }
    
    Node *tmp = head;
    while (tmp->next != NULL)
    {
        tmp = tmp->next;
    }
    // tmp ekhon last node e
    tmp->next = newNode;
    cout << "insterted at tail" << endl
         << endl;
}
void print_linked_list(Node *head)
{
    cout << endl;
    cout << "Your Linked List: ";
    Node *tmp = head;
    while (tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl
         << endl;
}
void insert_at_pos( Node* head, int pos, int v)
{
    Node* newnode = new Node(v);
    Node * temp=head;
    for(int i=0;i<=pos-1;i++)
    {
        temp=temp->next;
    }
    newnode->next=temp->next;
    temp->next=newnode;
    cout<<endl<<endl<<"inserted at position "<<pos<<endl<<endl;
}
void insert_at_head(Node * &head,int v)
{
    Node*newnode=new Node(v);
    newnode->next=head;
    head=newnode;
    cout<<endl<<"inserted at head"<<endl<<endl;
}
int main()
{
    Node *head = NULL;
    while (true)
    {
        cout << "Option 1: Insert at Tail" << endl;
        cout << "Option 2: Print Linked List" << endl;
        cout << "Option 3: insert at any position:" << endl;
        cout << "Option 4: insert at head" << endl;
        cout << "Option 5: Terminate" << endl;
        int op;
        cin >> op;
        if (op == 1)
        {
            cout << "Please enter value: ";
            int v;
            cin >> v;
            insert_at_tail(head, v);
        }
        else if (op == 2)
        {
            print_linked_list(head);
        }
        else if (op == 3)
        {
            int pos, v;
            cout << "Enter the position: ";
            cin >> pos;
            cout << "Enter the value: ";
            cin >> v;
            if(pos==0)
            {
                insert_at_head(head,v);
            }
            else
            {
                insert_at_pos(head,pos,v);
            }
           
        }
        else if(op==4)
        {
            int v;
            cout << "Enter the value: ";
            cin >> v;
            insert_at_head(head,v);
        }
        else if (op == 5)
        {
            break;
        }
    }
    return 0;
}