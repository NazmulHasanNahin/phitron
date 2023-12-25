#include <bits/stdc++.h>
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
class Queue
{
public:
        Node *head;
        Node *tail;
        Queue()
        {
            head = NULL;
            tail = NULL;
        }

    /*----------------- Public Functions of Queue -----------------*/

    bool isEmpty()
    {
        // Implement the isEmpty() function
        return head == NULL;
    }

    void enqueue(int val)
    {
        // Implement the enqueue() function
        Node *newNode = new Node(val);
        if (head == NULL)
        {
            head = newNode;
            tail = newNode;
            return;
        }
        tail->next = newNode;
        //tail = newNode; // warning to cheak again
        tail = tail->next;
    }

    int dequeue()
    {
        // Implement the dequeue() function
        // head pop kora;
        if (head == NULL)
        {
            return -1;
        }
        int rtrval = head->val;
        Node *dltnode = head;
        head = head->next;
        delete dltnode;
        return rtrval;
    }

    int front()
    {
        // Implement the front() function
        if (head == NULL)
        {
            return -1;
        }
        return head->val;
    }
};