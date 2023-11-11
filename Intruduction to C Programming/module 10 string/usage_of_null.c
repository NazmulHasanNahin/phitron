#include<stdio.h>
int main()
{
    char a[6]="nahin\0";        //'\0' is using as null.string ke stop koranor jonne ba garbage value na deoar jnne '\0' eta use kora hoy 
    printf("%s",a);
    return 0;
}