/*link:https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/D
*/
#include<stdio.h>
#include<string.h>
int main()
{
    char a[11];
    char b[11];
    scanf("%s %s",a,b);
    int a_leanth=strlen(a);
    int b_leanth=strlen(b);
    printf("%d %d\n",a_leanth,b_leanth);
    char add[22];
    strcpy(add,a);
    strcat(add,b);
    printf("%s\n",add);
    char temp=a[0];
    a[0]=b[0];
    b[0]=temp;
    printf("%s %s\n",a,b);
    return 0;
}