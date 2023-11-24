#include<bits/stdc++.h>
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
};
bool cmpr(student a,student b)
{
    if(a.eng_mrk != b.eng_mrk)
    {
        return a.eng_mrk>b.eng_mrk;
    }
    else if(a.mth_mark!=b.mth_mark)
    {
        return a.mth_mark>b.mth_mark;
    }
    else
    {
        return a.id<b.id;
    }
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
    sort(a,a+n,cmpr);
    for (int i = 0; i < n; i++)
    {
        cout << a[i].name << " " << a[i].cls << " " << a[i].sec << " " << a[i].id << " " << a[i].mth_mark << " " << a[i].eng_mrk << endl;
    }
    return 0;
}