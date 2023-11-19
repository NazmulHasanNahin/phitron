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
    person * nahin=new person("nahin",18);
    person * rakib=new person("rakib",20);
    *nahin=*rakib;
    delete rakib;
    cout<<nahin->name;
    return 0;
}