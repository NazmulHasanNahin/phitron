#include<bits/stdc++.h>
using namespace std;
int main()
{
    // string s="Nazmul Hasan Nahin";
    // string s;
    // cout<<s.size();
    // cout<<s.max_size();
    // cout<<s.capacity();

    // cout<<s<<endl;
    // s.clear();
    // cout<<s<<endl;

    // string s="nahin";
    // if(s.empty()==true) cout<<"khali"<<endl;
    // else cout<<"ase";

    string s;
    cin>>s;         /*input:hello_world*/
    s.resize(5);
    s.resize(8,'n');    /*hellonnn*/
    cout<<s;        /*hello*/


    return 0;
}