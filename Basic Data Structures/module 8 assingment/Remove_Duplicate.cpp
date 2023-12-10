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
void insert_tail(Node *&head, int val)
{
    Node *newNode = new Node(val);
    if (head == NULL)
    {
        head = newNode;
        return;
    }
    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}
void duplicate(Node *head)
{
    Node *tmp = head;
    while (tmp != NULL)
    {
        int currentVal = tmp->val;
        Node *tmp2 = tmp;
        while (tmp2 != NULL && tmp2->next != NULL)
        {
            if (tmp2->next->val == tmp->val)
            {
                Node *nextNode = tmp2->next;
                tmp2->next = tmp2->next->next;
                delete nextNode;
            }
            else
            {
                tmp2 = tmp2->next;
            }
        }

        tmp = tmp->next;
    }
}
void print_link_list(Node *head)
{
    Node *tmp = head;
    while (tmp != NULL)
    {
        cout << tmp->val << " ";
        tmp = tmp->next;
    }
    cout << endl;
}
int main()
{
    Node *head = NULL;
    int val;
    while (true)
    {
        cin >> val;
        if (val == -1)
        {
            break;
        }
        insert_tail(head,val);   
    }
    duplicate(head);
    print_link_list(head);
    return 0;
}