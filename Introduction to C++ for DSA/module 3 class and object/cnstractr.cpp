#include<bits/stdc++.h>
using namespace std;
class Student
{
public:
    int roll;
    int cls;
    int cg;
    Student(int roll, int cls, int cg)
    {
        this->roll=roll;
        this->cls=cls;
        this->cg=cg;

    }
};
int main()
{
    Student rahim(19, 9, 5.00);
    Student nahin(10,5,4.3);
    cout<<rahim.roll<<" "<<rahim.cg<<endl<<nahin.roll<<" "<<nahin.cg;
    return 0;
}