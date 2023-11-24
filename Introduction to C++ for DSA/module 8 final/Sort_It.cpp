#include <bits/stdc++.h>
using namespace std;
class student
{
public:
    string name;
    int cls;
    char sec;
    int id;
    int mth_mark;
    int eng_mrk;
    int total;
};
bool cmpr(student a, student b)
{
    if (a.total != b.total)
    {
        return a.total > b.total;
    }
    return a.id<b.id;
}

int main()
{
    int n;
    cin >> n;
    student a[n];

    for (int i = 0; i < n; i++)
    {
        cin >> a[i].name >> a[i].cls >> a[i].sec >> a[i].id >> a[i].mth_mark >> a[i].eng_mrk;
    }
    for(int i=0;i<n;i++)
    {
        a[i].total=(a[i].mth_mark+a[i].eng_mrk);
    }
    sort(a, a + n, cmpr);
    for (int i = 0; i < n; i++)
    {
        cout << a[i].name << " " << a[i].cls << " " << a[i].sec << " " << a[i].id << " " << a[i].mth_mark << " " << a[i].eng_mrk << endl;
    }
    return 0;
}