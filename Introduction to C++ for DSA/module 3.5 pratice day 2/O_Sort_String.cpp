#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    char ar[n];
    for(int i=0;i<n;i++)
    {
        cin>>ar[i];
    }
    sort(ar,ar+n);
    for(int i=0;i<n;i++)
    {
        cout<<ar[i];
    }
    return 0;
} 
// https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/O
// O. Sort string এই প্রব্লেমটি string declare করলে memory limit আসবে, সেইটি এইভাবে করুন।
// String এর size দেখুন 10^7, আর অনলাইন judge গুলো কোন array এর সাইজ 10^6 এর পর্যন্ত নেয় যাই, তাই এই প্রব্লেমটিতে character array দিয়ে string input না নিয়ে, string এর সাইজ বার loop চালিয়ে প্রতিবার একটা করে char input নিবেন এবং সেই char এর টিকে frequency array এর মধ্যে count করে রাখবেন, যেহেতু frequency array তে কোন character টি কতবার আসছে সেইটি count করে রাখছেন, তাহলে সেই frequency array এর মাধ্যমে character গুলোকে sorted ভাবে প্রিন্ট করতে পারবেন।
// int feq[123] = {0}
// for(int i=0; i<n; i++)
// {
// char ch;
// cin>>ch;
// feq[ch]++;
// }
// এই feq টা use করে আপনি তারপর character গুলো প্রিন্ট করতে পারবেন।