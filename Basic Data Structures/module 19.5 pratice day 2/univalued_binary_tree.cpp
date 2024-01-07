/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool crnt(TreeNode* root,int a)
    {
        if(root==NULL)
        {
            return true;
        }
        if(root->val!=a)
        {
            return false;
        }
        return crnt(root->left,a) && crnt(root->right,a);
    }
    bool isUnivalTree(TreeNode* root)
    {
        int a=root->val;
        return crnt(root,a);
    }
};