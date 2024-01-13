#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    cin.ignore();
    for (int i = 0; i < t; i++)
    {
        string s;
        getline(cin, s);
        stringstream ss(s);
        map<string, int> mp;
        string word;
        string most;
        int time = 0;
        while (ss >> word)
        {
            mp[word]++;
            if (mp[word] > time)
            {
                time = mp[word];
                most = word;
            }
        }
        cout << most << " " << time << endl;
    }
    return 0;
}