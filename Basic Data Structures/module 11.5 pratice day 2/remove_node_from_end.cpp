#include<bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int size_(ListNode* head) {
        ListNode* tmp = head;
        int cnt = 0;
        while (tmp != NULL) {
            cnt++;
            tmp = tmp->next;
        }
        return cnt;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = size_(head);
        
        if (size == n) {
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }

        ListNode* newHead = head;
        ListNode* current = newHead;

        for (int i = 0; i < size - n - 1; ++i) {
            current = current->next;
        }

        ListNode* temp = current->next;
        current->next = temp->next;
        delete temp;

        return newHead;
    }
};
