#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    stack<int>st;
    queue<int>q;
    for(int i=0;i<n;i++)
    {                   //stk
        int val;
        cin>>val;
        st.push(val);
    }
    for(int i=0;i<m;i++)
    {
        int val;        //q
        cin>>val;
        q.push(val);
    }
    while(!st.empty() && !q.empty())
    {
        if(st.top()==q.front())
        {
            st.pop();
            q.pop();
        }
        else
        {
            cout<<"NO";
            return 0;
        }
    }
    if(q.empty() && st.empty())
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    return 0;
}