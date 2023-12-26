// https://www.codingninjas.com/studio/problems/min-stack_3843991
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

class minStack
{
public:
    stack<int> s;
    Node *head;
    Node *tail;
    int min;
    minStack()
    {
        head = NULL;
        tail = NULL;
        min = INT_MAX;
    }
    void push(int num)
    {
        if (head == NULL)
        {
            head = new Node(num);
            tail = head;
            s.push(num);
            min = num;
        }
        else
        {
            Node *newNode = new Node(num);
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
            s.push(num);
            if (num < min)
            {
                min = num;
            }
        }
    }
    int pop()
    {
        if (head == NULL)
        {
            return -1;
        }
        int popped = head->val;
        Node *temp = head;
        if (head == tail)
        {
            head = NULL;
            tail = NULL;
        }
        else
        {
            head = head->next;
            head->prev = NULL;
        }
        delete temp;
        s.pop();
        if (s.empty())
        {
            min = INT_MAX;
        }
        else if (popped == min)
        {
            stack<int> tempStack;
            min = s.top();
            while (!s.empty())
            {
                min = min < s.top() ? min : s.top();
                tempStack.push(s.top());
                s.pop();
            }
            while (!tempStack.empty())
            {
                s.push(tempStack.top());
                tempStack.pop();
            }
        }
        return popped;
    }

    int top()
    {
        if (head == NULL)
        {
            return -1;
        }
        return head->val;
    }

    int getMin()
    {
        if (head == NULL)
        {
            return -1;
        }
        return min;
    }
};
