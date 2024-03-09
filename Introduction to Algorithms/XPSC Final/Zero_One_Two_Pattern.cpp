#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= (2 * n) - 1; i++)
    {
        int num = (i - 1) % 3;
        int spacesbeforenumber;
        if (i <= n)
        {
            spacesbeforenumber = i - 1;
        }
        else
        {
            spacesbeforenumber = 2 * n - i - 1;//range
        }
        for (int j = 0; j < spacesbeforenumber; j++)
        {
            cout << " ";
        }
        if (num == 2)
        {
            cout << 0;
        }
        else
        {
            cout << num + 1;
        }
        if (i != n)
        {
            int spacebetweennumnum = 2 * (n - spacesbeforenumber) - 3;
            for (int j = 0; j < spacebetweennumnum; j++)
            {
                cout << " ";
            }
            if (num == 2)
            {
                cout << 0;
            }
            else
            {
                cout << num + 1;
            }
        }
        cout << endl;
    }
    return 0;
}
