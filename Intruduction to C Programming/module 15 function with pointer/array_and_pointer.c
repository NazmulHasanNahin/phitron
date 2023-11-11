#include<stdio.h>
int main()
{
    int ar[5]={10,20,30,40,50};
    printf("0th er adress %p\n",&ar[0]);        //adress of ar[0]
    printf("0th er adress %p\n",ar);        //adress of ar
    printf("0th er adress %d\n",*ar);           //dereference of ar
    printf("1st indx er value %d\n",*(ar+1));
    printf("%d\n",*(ar+1));
    printf("%d\n",*(1+ar));             //all the 4 are same 
                                        //array is also pointer
    printf("%d\n",(ar[1]));
    printf("%d\n",(1[ar]));
    return 0;
}