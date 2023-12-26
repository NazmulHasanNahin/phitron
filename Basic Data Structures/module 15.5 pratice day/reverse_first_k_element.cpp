#include <bits/stdc++.h> 
queue<int> reverseElements(queue<int>q, int k)
{
    stack<int>s;
    for(int i=0;i<k;i++)
    {
        int x=q.front();
        q.pop();
        s.push(x);
    }
    while(!s.empty())
    {
        int x=s.top();
        s.pop();
        q.push(x);
    }
    int x=q.size()-k;
    for(int i=0;i<x;i++)
    {
        int y=q.front();
        q.pop();
        q.push(y);
    }
    return q;
}
// https://www.codingninjas.com/studio/problems/reverse-first-k-elements-of-queue_982771