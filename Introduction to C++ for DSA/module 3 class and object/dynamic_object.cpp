#include<bits/stdc++.h>
using namespace std;
class student
{
    public:
    int roll;
    int cls;
    double cg; 
    student(int roll,int cls,double cg)
    {
        this->roll=roll;
        this->cls=cls;
        this->cg=cg;
    }
};
int main()
{
    student rahim(672751,9,3.2);
    student* stdnt_pntr=new student(672751,9,3.2);
    cout<<((stdnt_pntr)->roll);
    return 0;
}