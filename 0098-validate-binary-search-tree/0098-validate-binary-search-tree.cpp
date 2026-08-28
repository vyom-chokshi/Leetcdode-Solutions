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

    bool dfs(TreeNode* root,long long low,long long max)
    {
        if(root==NULL)
        {
            return true;
        }

        if(root->val <= low || root->val >= max)
        {
            return false;
        }

        bool left = dfs(root->left, low, root->val);
        bool right = dfs(root->right, root->val, max);

        return left && right;


    }

    bool isValidBST(TreeNode* root) 
    {
        return dfs(root,LLONG_MIN,LLONG_MAX);   
    }
};