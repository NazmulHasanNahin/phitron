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
void printlevelnode(Node *root, int x)
{
    if (root == NULL)
    {
        cout << "Invalid" << endl;
        return;
    }
    queue<Node *> q;
    q.push(root);
    int lvl = 0;
    while (!q.empty())
    {
        int sz = q.size();
        if (lvl == x)
        {
            for (int i = 0; i < sz; i++)
            {
                Node *parent = q.front();
                q.pop();
                cout << parent->val << " ";
            }
            cout << endl;
            return;
        }
        for (int i = 0; i < sz; i++)
        {
            Node *parent = q.front();
            q.pop();
            if(parent->left)
            {
                q.push(parent->left);
            }
            if(parent->right)
            {
                q.push(parent->right);
            }
        }
        lvl++;
    }
    cout<<"Invalid"<<endl;
}
int main()
{
    Node *root = input_tree();
    int x;
    cin>>x;
    printlevelnode(root,x);
    return 0;
}