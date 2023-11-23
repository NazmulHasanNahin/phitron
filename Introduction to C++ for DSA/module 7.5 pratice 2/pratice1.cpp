#include<bits/stdc++.h>
using namespace std;
class student
{
    public:
        string name;
        int roll;
        int mark;
};
bool cmpr(student a,student b)
{
    if(a.mark!=b.mark)
    {
        return a.mark > b.mark;
    }
    return a.roll<b.roll;
}

int main()
{
    int n;
    cin>>n;
    student a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i].name>>a[i].roll>>a[i].mark;
    }
    sort(a,a+n,cmpr);
    for (int i = 0; i < n; i++)
    {
        cout << a[i].name<<" "<<a[i].roll<<" "<< a[i].mark<<endl;
    }
    return 0;
}
// https://docs.google.com/document/d/1njDKQisp_wc59vWoK4c7cml-cWfg77tk/edit