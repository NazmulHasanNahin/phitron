#include <bits/stdc++.h>
using namespace std;
class student
{
public:
    string name;
    int age, marks;
    student(string name, int age, int marks)
    {
        this->name = name;
        this->age = age;
        this->marks = marks;
    }
};
class cmp
{
public:
    bool operator()(student a, student b)
    {
        if (a.marks != b.marks)
        {
            return a.marks < b.marks;
        }
        else
        {
            return a.age > b.age;
        }
    }
};
int main()
{
    int t;
    cin >> t;
    string name;
    int age, marks;
    priority_queue<student, vector<student>, cmp> pq;
    for (int i = 0; i < t; i++)
    {
        cin >> name >> age >> marks;
        pq.push({name, age, marks});
    }
    int test;
    cin >> test;
    for (int i = 0; i < test; i++)
    {
        int x;
        cin >> x;
        if (x == 0)
        {
            cin >> name >> age >> marks;
            pq.push({name, age, marks});
            cout << pq.top().name << " " << pq.top().age << " " << pq.top().marks << endl;
        }
        else if (x == 1)
        {
            if (pq.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << pq.top().name << " " << pq.top().age << " " << pq.top().marks << endl;
            }
        }
        else if (x == 2)
        {
            if (pq.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                pq.pop();
                if (pq.empty())
                {
                    cout << "Empty" << endl;
                }
                else
                {
                    cout << pq.top().name << " " << pq.top().age << " " << pq.top().marks << endl;
                }
            }
        }
    }
    return 0;
}