/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int max(int m, int n) {
    if (m >= n) {
        return m;
    }

    return n;
}

int maxDepth(struct TreeNode* root) {
    if (root == NULL) {
        return 0;
    }

    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}