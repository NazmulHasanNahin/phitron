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
student * fun()
{
    student rahim(672751,9,3.2);
    student *p=&rahim;
    return p;
}
int main()
{
    student * ans=fun();
    cout<<(*ans).cg;
    return 0;
}