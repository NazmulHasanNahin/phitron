/*Given a string S. Determine how many times does each letter occurred in S.

Input
Only one line contains the string S (1 ≤ |S| ≤ 107) where |S| is the length of the string and it consists of only lowercase English letters.

Output
For each character that appears in S, print a single line that contains the following format: "X : Y" where X is the letter and Y is the number of times that letter X occurred in S.

Note: you must print letters in ascending order.
https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J
*/
#include <stdio.h>
int main()
{
    char c;
    int count[26] = {0};
    while (scanf("%c", &c) != EOF)
    {
        count[c - 'a']++;
    }
    for (char i = 'a'; i <= 'z'; i++)
    {
        if (count[i - 'a'] > 0)
        {
            printf("%c : %d\n", i, count[i - 'a']);
        }
    }
    return 0;
}