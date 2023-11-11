/*Timon has a
 candies and his friend, Pumbaa, has b
 candies, so Pumbaa asked Timon to tell him the value of a−b
. However, Timon will tell him the value of a−b
 if the value is ≥0
; otherwise, he will lie and say 0
. Since it was a hard task for Timon, he's asking for your help.

Given two numbers a
 and b
, find the answer.

Input
Only one line containing two numbers a,b
 (1≤a,b≤109
).

Output
Print the answer as specified in the statement.
link:https://codeforces.com/group/MWSDmqGsZm/contest/326907/problem/A
input:9 1
*/ 
#include <stdio.h>

int main() {
    int  a, b;
    scanf("%d %d", &a, &b);

    if (a - b >= 0) {
        printf("%d\n", a - b);
    } else {
        printf("0\n");
    }

    return 0;
}
