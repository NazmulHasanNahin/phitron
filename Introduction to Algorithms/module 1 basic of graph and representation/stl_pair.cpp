#include <bits/stdc++.h>
using namespace std;
class pair_
{
public:
    int first, second;
    void make_pair(int a, int b)
    {
        first = a;
        second = b;
    }
};
int main()
{
    pair_ p;
    p.make_pair(10, 20);
    cout << p.first << " " << p.second << " ";
    return 0;
}
//custom make