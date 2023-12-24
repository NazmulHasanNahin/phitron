#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    queue<string>q;
    while(t--)
    {
        int x;
        cin>>x;
        string nm;
        if(x==0)
        {
            cin>>nm;
            q.push(nm);
        }
        else if(x==1)
        {
            if(!q.empty())
            {
                cout<<q.front()<<endl;
                q.pop();
            }
            else
            {
                cout<<"Invalid"<<endl;
            }
        }
    }
    return 0;
}