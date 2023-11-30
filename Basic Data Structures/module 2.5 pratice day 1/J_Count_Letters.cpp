#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin >> s;
    // cout << s;
    int word = 26;
    vector<int> a(word, 0);
    for(char x:s)
    {
        // cout<<x<<" ";
        a[x-'a']++;
    }
    for(int i=0;i<26;i++)
    {
        if(a[i]>0)
        {
            cout<<char('a'+i)<<" "<<":"<<" "<<a[i]<<endl;
        }
    }
    return 0;
}