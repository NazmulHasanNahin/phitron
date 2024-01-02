/*
    Following is Binary Tree Node structure:
    class TreeNode
    {
    public:
        int data;
        TreeNode *left, *right;
        TreeNode() : data(0), left(NULL), right(NULL) {}
        TreeNode(int x) : data(x), left(NULL), right(NULL) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : data(x), left(left), right(right) {}
    };
*/
vector<int>v;
void inorder(TreeNode* root)
{
    if(root==NULL)
    {
        return;
    }
    inorder(root->left);
    v.push_back(root->data);
    inorder(root->right);

}
vector<int> getInOrderTraversal(TreeNode *root)
{
    // Write your code here.
    v.clear();
    inorder(root);
    return v;
}