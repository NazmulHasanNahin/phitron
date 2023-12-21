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

int main()
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
        Node *newNode = new Node(val);
        if (head == NULL)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }
    Node *i = head;
    Node *j = tail;
    bool palindrm = true;
    while (i != j)
    {
        if (i->val != j->val)
        {
            palindrm = false;
            break;;
        }
        i = i->next;
        j = j->prev;
    }
    if (palindrm == true)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}