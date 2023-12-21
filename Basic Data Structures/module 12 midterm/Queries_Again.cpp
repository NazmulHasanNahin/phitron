#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *next;
    Node *prev;
    Node(int val)
    {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};
void insert_at_head(Node *&head, Node *&tail, int val)
{
    Node *newNode = new Node(val);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
    }
    else
    {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
}
void insert_at_tail(Node *&head, Node *&tail, int val)
{
    Node *newNode = new Node(val);
    if (tail == NULL)
    {
        head = newNode;
        tail = newNode;
    }
    else
    {
        newNode->prev = tail;
        tail->next = newNode;
        tail = newNode;
    }
}
void insert_at_any_pos(Node *&head, Node *&tail, int &size, int pos, int val)
{
    if (pos < 0 || pos > size)
    {
        cout << "Invalid" << endl;
        return;
    }
    Node *newNode = new Node(val);
    if (pos == 0)
    {
        insert_at_head(head, tail, val);
        size++;
        return;
    }
    else if (pos == size)
    {
        insert_at_tail(head, tail, val);
        size++;
        return;
    }
    Node *cur = head;
    for (int i = 0; i < pos - 1; i++)
    {
        cur = cur->next;
    }
    newNode->prev = cur;
    newNode->next = cur->next;
    cur->next->prev = newNode;
    cur->next = newNode;
    size++;
}
void print_linked_list(Node *head, Node *tail)
{
    Node *cur = head;
    cout << "L -> ";
    while (cur)
    {
        cout << cur->val << " ";
        cur = cur->next;
    }
    cout << endl;
    cur = tail;
    cout << "R -> ";
    while (cur)
    {
        cout << cur->val << " "; // ulta
        cur = cur->prev;
    }
    cout << endl;
}
int main()
{
    Node *head = NULL;
    Node *tail = NULL;
    int size = 0;
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int x, v;
        cin >> x >> v;
        if (x < 0 || x > size || v < 0 || v > 1000)
        {
            cout << "Invalid" << endl;
            continue;
        }
        insert_at_any_pos(head, tail, size, x, v);
        print_linked_list(head, tail);
    }
    return 0;
}