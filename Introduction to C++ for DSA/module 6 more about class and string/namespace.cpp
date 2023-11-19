#include<bits/stdc++.h>
using namespace std;
namespace nahin
{
    int age=18;
    void hello()
    {
        cout<<"nahin from namespace";
    }
    
}
namespace sakib
{
    int age1=20;
    void hello1()
    {
        cout<<"sakib from namespace 1";
    }
    
}
using namespace nahin;
using namespace sakib;
int main()
{
    // cout<<nahin::age<<endl;
    // cout<<sakib::age1;
    cout<<age<<endl;
    cout<<age1;
    return 0;
}