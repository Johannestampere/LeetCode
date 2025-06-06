/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* orig = root;
        int pval = p->val;
        int qval = q->val;
        while (root) {
            if (pval < root->val && qval < root->val) {
                root = root->left;
            } else if (pval > root->val && qval > root->val) {
                root = root->right;
            } else {
                return root;
            }
        }
        return orig;
    }

};