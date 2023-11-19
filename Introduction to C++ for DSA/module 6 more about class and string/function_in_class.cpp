#include<bits/stdc++.h>
using namespace std;
class person
{
    public:
        string name;
        int age;
        person(string nm,int ag)
        {
            name=nm;
            age=ag;
        }
        void hello()
        {
            cout<<name<<" "<<age;
        }
};
int main()
{
    person nahin("nazmul hasan nahin",18);
    nahin.hello();
    // cout<<nahin.name<<endl;
    return 0;
}