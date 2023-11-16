#include<bits/stdc++.h>
using namespace std;
int main()
{
    string line;
    while(getline(cin,line))
    {
        string srln;
        for(char wrd:line)
        {
            if (wrd!=' ')
            {
                srln+=wrd;
            }
        }
        sort(srln.begin(), srln.end());
        cout << srln << endl;
    }
    return 0;
}