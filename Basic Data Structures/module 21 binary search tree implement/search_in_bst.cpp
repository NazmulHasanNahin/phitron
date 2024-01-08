#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
        int val;
        Node* left;
        Node* right;
    Node(int val)
    {
        this->val=val;
        this->left=NULL;
        this->right=NULL;
    }
};
Node *input_tree()
{
    int val;
    cin >> val;
    Node *root;
    if (val == -1)
    {
        root = NULL;
    }
    else
    {
        root = new Node(val);
    }
    queue<Node *> q;
    if (root)
        q.push(root);
    while (!q.empty())
    {
        Node *parent = q.front(); // 1
        q.pop();

        int l, r; // 2
        cin >> l >> r;
        Node *left = NULL;
        Node *right = NULL;
        if (l != -1)
        {
            left = new Node(l);
            q.push(left);
        }
        if (r != -1)
        {
            right = new Node(r);
            q.push(right);
        }
        parent->left = left;
        parent->right = right;
    }
    return root;
}
bool search(Node* root,int x)
{
    if(root==NULL) return false;
    if(root->val==x) return true;
    if(x<root->val)
    {
        return search(root->left,x);
    }
    else
    {
        return search(root->right,x);
    }
}
int main()
{
    Node* root=input_tree();
    if(search(root,6))
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }
    return 0;
}