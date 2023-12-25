void reverseStack(stack<int> &s) 
{
    if(s.empty()) return;
    int x=s.top();
    s.pop();
    reverseStack(s);
    stack<int>ns;
    while(!s.empty())
    {
        ns.push(s.top());
        s.pop();
    }
    ns.push(x);
    while(!ns.empty())
    {
        s.push(ns.top());
        ns.pop();
    }
}
// https://www.codingninjas.com/studio/problems/reverse-stack-using-recursion_631875