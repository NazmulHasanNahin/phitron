#include <bits/stdc++.h>
using namespace std;
class ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
void deleteNode(ListNode *node)
{
    node->val=node->next->val;
    ListNode * deleteNode=node->next;
    node->next=node->next->next;
}
int main()
{

    return 0;
}