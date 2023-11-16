#include <bits/stdc++.h>
using namespace std;
class Student
{
public:
    char name[100];
    int roll;
    char secion;
    int math_mark;
    int cls;
    Student(char *name, int roll, char section, int math_mark, int cls)
    {
        strcpy(this->name, name);
        this->roll = roll;
        this->secion = section;
        this->math_mark = math_mark;
        this->cls = cls;
    }
};
int main()
{
    Student first("nahin", 672751, 'b', 90, 12);
    cout << first.name;
    return 0;
}
