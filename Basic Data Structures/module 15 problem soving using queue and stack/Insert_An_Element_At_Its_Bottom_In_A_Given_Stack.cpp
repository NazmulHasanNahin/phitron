// https://www.codingninjas.com/studio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166
#include <bits/stdc++.h> 
stack<int> pushAtBottom(stack<int>& st, int x) 
{
    stack<int> newst;
    while(!st.empty())
    {
        newst.push(st.top());
        st.pop();
    }
    newst.push(x);
    while(!newst.empty())
    {
        st.push(newst.top());
        newst.pop();
    }
    return st;
}
