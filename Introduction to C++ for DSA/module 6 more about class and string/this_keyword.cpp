#include<bits/stdc++.h>
using namespace std;
class person
{
    public:
        string name;
        int age;
        person(string name,int age)
        {
            this->name=name;
            this->age=age;
        }
};
int main()
{
    person nahin("nahin",18);
    cout<<nahin.age<<" "<<nahin.name<<endl;
    return 0;
}