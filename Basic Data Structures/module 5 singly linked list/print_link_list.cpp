#include<bits/stdc++.h>
using namespace std;
class node
{
    public:
        int value;
        node* next;
        node(int value)
        {
            this->value=value;
            this->next=NULL;
        }
};
int main()
{
    node * head=new node(10);
    node * a=new node(20);
    node * b=new node(30);
    node * c=new node(40);
    node * d=new node(50);

    head->next=a;
    a->next=b;
    b->next=c;
    c->next=d;


    // cout<<head->value<<endl;
    // cout<<head->next->value<<endl;
    // cout<<head->next->next->value<<endl;
    // cout<<head->next->next->next->value<<endl;

    // while(head != NULL)
    // {    
    //     cout<<head->value<<endl;         //not recomanded head haraia jay
    //     head=head->next;
    // }


    node*temp=head;
    while(temp != NULL)
    {    
        cout<<temp->value<<endl;        
        temp=temp->next;
    }
    temp=head;                  //jodi 2 bar print korte chaii
    while(temp != NULL)
    {    
        cout<<temp->value<<endl;        
        temp=temp->next;
    }
    return 0;

}