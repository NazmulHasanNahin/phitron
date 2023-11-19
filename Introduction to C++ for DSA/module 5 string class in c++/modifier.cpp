#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a="hello";
    string b="gello";
    // // a=a+b;
    // // a+=b;
    // a.append(b);
    // cout<<a;

    // a.push_back('a');       /*add character to the last of the string.*/
    // a.pop_back();   /*remove the last character of the string.*/
    // cout<<a;

    string c="helloworld";
    // c.erase(4);     /*to dlt all after given index*/
    // c.erase(4,1);       /*dlt desire index value*/
    // cout<<c;    

    // c.replace(4,3,"nahi");

    c.insert(5,"nahin");
    cout<<c;
    return 0;
}
