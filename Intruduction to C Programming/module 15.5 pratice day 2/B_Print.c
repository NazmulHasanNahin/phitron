#include<stdio.h>
void func(int n)
{
    for(int i=1;i<=n;i++)
    {
        printf("%d",i);
        if (i != n)
        {
            printf(" ");
        }
        // return res;
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    func(n);
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/B
// also sloved bt this way
// #include<stdio.h>
// void func(int n)
// {
//     for(int i=1;i<=n;i++)
//     {
//         printf("%d ",i);
//         // return res;
//     }
// }
// int main()
// {
//     int n;
//     scanf("%d",&n);
//     if(n<=1000)
//     {
//         func(n);
//     }
    
//     return 0;
// }
// // https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/B