#include<bits/stdc++.h>
using namespace std;
class crickter
{
public:
    int jersy_no;
    string country;

};
int main()
{
    crickter*dhoni=new crickter;
    dhoni->jersy_no=7;
    dhoni->country="India";
    crickter*kholi=new crickter;
    kholi->jersy_no=dhoni->jersy_no;
    kholi->country=dhoni->country;
    delete dhoni;
    cout<<kholi->jersy_no<<endl;
    cout<<kholi->country<<endl;
    return 0;
}