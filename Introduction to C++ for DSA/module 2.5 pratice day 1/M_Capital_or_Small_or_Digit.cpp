#include<bits/stdc++.h>
using namespace std;
int main()
{
    char a;
    cin>>a;
    if(a >='0' && a<='9')
    {
        cout<<"IS DIGIT"<<endl;
    }
    else if(a>='A' && a<='Z')
    {
        cout<<"ALPHA"<<endl<<"IS CAPITAL"<<endl;
    }
    else if(a>='a'&& a<='z')
    {
        cout<<"ALPHA"<<endl<<"IS SMALL"<<endl;
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/M