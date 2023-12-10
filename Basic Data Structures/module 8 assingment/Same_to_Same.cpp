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
int size(Node *head)
{
    int sz = 0;
    Node *tmp = head;
    while (tmp != NULL)
    {
        sz++;
        tmp = tmp->next;
    }
    return sz;
}

int main()
{
    Node *head = NULL;
    Node *tail = NULL;
    Node *head1 = NULL;
    Node *tail1 = NULL;
    int val;
    while (true)
    {
        cin >> val;
        if (val == -1) // 1st
        {
            break;
        }
        insert_tail(head, tail, val);
    }
    while (true)
    {
        cin >> val;
        if (val == -1) // 2nd in
        {
            break;
        }
        insert_tail(head1, tail1, val);
    }
    int sz = size(head);
    int sz1 = size(head1);
    if (sz != sz1)
    {
        cout << "NO";
        return 0;
    }
    else
    {
        Node *tmp = head;
        Node *tmp1 = head1;
        bool flag = true;

        while (tmp != NULL)
        {
            if (tmp->val != tmp1->val)
            {
                flag = false;
                break;
            }
            tmp = tmp->next;
            tmp1 = tmp1->next;
        }
        if(flag==true)
        {
            cout<<"YES";
        }
        else
        {
            cout<<"NO";
        }
    }
    return 0;
}