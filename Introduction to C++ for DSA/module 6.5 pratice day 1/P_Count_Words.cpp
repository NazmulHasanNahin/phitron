#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin,s);
    // cout<<s;
    bool inside_word=false;
    int count=0;
    for (char c:s)
    {
        if(isalpha(c))
        {
            if(inside_word==false)
            {
                count++;
            }
            inside_word=true;
        }
        else
        {
            inside_word=false;
        }
        
    }
    cout<<count<<endl;
    return 0;
}

// https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/P