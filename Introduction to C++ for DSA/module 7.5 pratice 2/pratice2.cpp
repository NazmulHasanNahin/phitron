#include<bits/stdc++.h>
using namespace std;
class student
{
    public:
        string name;
        int roll;
        int mark;
};
int main()
{
    int n;
    cin>>n;
    student a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i].name>>a[i].roll>>a[i].mark;
    }
    for(int i=0;i<n/2;i++)
    {
        swap(a[i],a[n-1-i]);
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i].name<<" "<<a[i].roll<<" "<< a[i].mark<<endl;
    }
    return 0;
}