#include<stdio.h>
#include<string.h>
int main()
{
    char a[1001],b[1001];
    scanf("%s %s",a,b);
    strcpy(b,a);
    // printf("%s",b);
    int i=0,j=strlen(b)-1;
    while (i<j)
    {
        char temp=b[i];
        b[i]=b[j];
        b[j]=temp;
        i++;
        j--;
    }
    if(strcmp(a,b)==0)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
      
    return 0;
}
// https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/I