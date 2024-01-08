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
void insert(Node* & root,int x)
{
    if(root==NULL)
    {
        root=new Node(x);
        return;
    }
    if(x<root->val)
    {
        if(root->left==NULL)
        {
            root->left=new Node(x);
        }
        else
        {
            insert(root->left,x);
        }
    }
    else
    {
        if(root->right==NULL)
        {
            root->right=new Node(x);
        }
        else
        {
            insert(root->right,x);
        }
    }
}
void level_order(Node *root)
{
    if (root == NULL)
    {
        cout << "Tree nai" << endl;
        return;
    }
    queue<Node *> q;
    q.push(root);
    while (!q.empty())
    {
        // 1. ber kore ana
        Node *f = q.front();
        q.pop();

        // 2. jabotiyo ja kaj ache
        cout << f->val << " ";

        // 3. tar children gulo ke rakha
        if (f->left)
            q.push(f->left);
        if (f->right)
            q.push(f->right);
    }
}
int main()
{
    Node* root=input_tree();
    int x;
    cin>>x;
    insert(root,x);
    level_order(root);
    return 0;
}