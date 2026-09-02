/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool dfs(struct TreeNode* left, struct TreeNode* right) {

    /*
    Depth-first search structure that utilizes recurisve
    pattern to ultimately check for mirrors in the binary
    tree. Returns the appropriate response per the prompt 
    */
    
    if (!left && !right) {return true;}
    if (!left || !right) {return false;}
    if (left->val != right->val) {return false;}

    return (dfs(left->left, right->right) && dfs(left->right, right->left));
}

bool isSymmetric(struct TreeNode* root) {
    
    return dfs(root->left, root->right);

}

// Time Complexity -> O(N) as n is the number of elements in the root
// Space Complexity -> O(1) as auxillary space remains constant
