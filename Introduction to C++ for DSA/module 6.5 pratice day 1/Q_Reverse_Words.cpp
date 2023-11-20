#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    stringstream ss(s);
    string word;
    // cout<<s;
    if (ss >> word)
    {
        reverse(word.begin(), word.end());
        cout << word;
    }
    while (ss >> word)
    {
        cout << " ";
        reverse(word.begin(), word.end());
        cout << word;
    }
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q