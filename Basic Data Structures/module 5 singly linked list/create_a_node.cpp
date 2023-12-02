#include<bits/stdc++.h>
using namespace std;
class node
{
    public:
        int value;
        node* next;
};
int main()
{
    node a,b;
    a.value=10;
    b.value=20;


    a.next=&b;      
    b.next=NULL;


    cout<<a.value<<endl;
    cout<<a.next->value;
    return 0;
}