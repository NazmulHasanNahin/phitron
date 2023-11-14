#include<bits/stdc++.h>
using namespace std;
class student
{
    public:
    char name[100];
    int roll;
    double cg;
};
int main()
{
    student a,b;
    // a.roll=672751;
    // a.cg=3.25;
    // char temp[100]="nahin";
    // strcpy(a.name,temp);
    // cout<<a.name<<" "<<a.cg<<" "<<a.roll;
    cin.getline(a.name,100);
    cin>>a.roll>>a.cg;
    getchar();
    cin.getline(b.name,100);
    cin>>b.roll>>b.cg;
    cout<<a.name<<" "<<a.cg<<" "<<a.roll<<endl;
    cout<<b.name<<" "<<b.cg<<" "<<b.roll;
    return 0;
}
