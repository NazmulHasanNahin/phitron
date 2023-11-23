#include <bits/stdc++.h>
using namespace std;
int main()
{
    
    string s;
    getline(cin, s);
    stringstream ss(s);
    string itrt;
    int found=0;
    string word="Jessica"; 
    while (ss >> itrt)
    {
        
        if(itrt==word)
        {
            found=1;
            break;
        }
    }
    if (found==1)
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    // cout<<ss<<endl;
    return 0;
}