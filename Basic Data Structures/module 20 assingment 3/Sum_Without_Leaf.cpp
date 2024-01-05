#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    Node *left;
    Node *right;
    Node(int val)
    {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
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
        Node *left;
        Node *right;
        if (l == -1)
        {
            left = NULL;
        }
        else
        {
            left = new Node(l);
        }
        if (r == -1)
        {
            right = NULL;
        }
        else
        {
            right = new Node(r);
        }
        parent->left = left;
        parent->right = right;
        // 3
        if (parent->left)
        {
            q.push(parent->left);
        }
        if (parent->right)
        {
            q.push(parent->right);
        }    
    }
    return root;
}
int sum(Node* root)
{
    if(root==NULL)
    {
        return 0;//ssh
    }
    if(root->left == NULL && root->right==NULL)
    { 
        return 0;
    }
    return (root->val+sum(root->left)+sum(root->right));
}
int main()
{
    Node *root = input_tree();
    int res=sum(root);
    cout<<res<<endl;
    return 0;
}