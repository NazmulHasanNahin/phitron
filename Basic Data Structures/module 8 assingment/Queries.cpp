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
void insert_head(Node *&head, int val)
{
    Node *newNode = new Node(val);
    newNode->next = head;
    head = newNode;
}
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
void dlt_in_indx(Node *&head, int pos)
{
    if (head == NULL || pos < 0)
    {
        return;
    }
    if (pos == 0)
    {
        Node *tmp = head;
        head = head->next;
        delete tmp;
        return;
    }
    Node* tmp = head;
    for (int i = 0; tmp != NULL && i < pos - 1; ++i)
    {
        tmp = tmp->next;
    }

    if (tmp == NULL || tmp->next == NULL)
        return;

    Node* dlt = tmp->next;
    tmp->next = tmp->next->next;
    delete dlt;
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
    int q;
    cin >> q;
    Node *head = NULL;
    for (int i = 0; i < q; i++)
    {
        int x, v;
        cin >> x >> v;
        if (x == 0)
        {
            insert_head(head, v);
        }
        else if (x == 1)
        {
            insert_tail(head, v);
        }
        else if (x == 2)
        {
            dlt_in_indx(head, v);
        }
        print_link_list(head);
    }
    return 0;
}