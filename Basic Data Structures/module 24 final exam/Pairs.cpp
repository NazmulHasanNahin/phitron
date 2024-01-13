#include <bits/stdc++.h>
using namespace std;
class student
{
public:
    string name;
    int val;
    student(string name, int val)
    {
        this->name = name;
        this->val = val;
    }
};
class cmp
{
public:
    bool operator()(student a, student b)
    {
        if (a.name != b.name)
        {
            return a.name > b.name;
        }
        return a.val < b.val;
    }
};
int main()
{
    int t;
    cin >> t;
    priority_queue<student,vector<student>,cmp>pq;
    for (int i = 0; i < t; i++)
    {
        string name;
        int val;
        cin >> name >> val;
        student obj(name,val);
        pq.push(obj);
    }
    while(!pq.empty())
    {
        cout<<pq.top().name<<" "<<pq.top().val<<endl;
        pq.pop();
    }
    return 0;
}