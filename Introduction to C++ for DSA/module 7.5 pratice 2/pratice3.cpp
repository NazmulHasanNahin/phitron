#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    string word;
    cin >> word;
    stringstream ss(s);
    int count = 0;
    string itert;
    while (ss >> itert)
    {
        if (itert == word)
        {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}