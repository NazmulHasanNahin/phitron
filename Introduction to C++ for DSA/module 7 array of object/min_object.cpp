#include <bits/stdc++.h>
using namespace std;
class student
{
public:
    string name;
    int roll;
    int marks;
};
int main()
{
    int n;
    cin >> n;
    student a[n];
    for (int i = 0; i < n; i++)
    {
        // cin.ignore();
        // getline(cin, a[i].name);
        cin >>a[i].name>> a[i].roll >> a[i].marks;
    }
    student mn;
    mn.marks = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        if (a[i].marks < mn.marks)
        {
            mn = a[i];
        }
    }
    cout << mn.name;
    return 0;
}