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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> st; // keep track of visited nodes

        while (root || !st.empty()) {
            // traverse as far left as possible
            if (root) {
                st.push(root);
                root = root->left;
            }
            else { // if not possible to go left anymore, pop min element from stack and --k
                root = st.top();
                st.pop();
                
                --k;
                if (k == 0) return root->val;
                root = root->right;
            }

        }

        return -1;
    }
};