/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int dfs(struct TreeNode* root, int length) {

    /*
    Recursively checks each node for the deepest
    search length, returns the max.
    */

    if (!root) {return length;}
    
    length += 1;
    int max = dfs(root->left, length);
    int max_r = dfs(root->right, length);

    if (max_r > max) {max = max_r;}

    return max;
}

int maxDepth(struct TreeNode* root) {

    if (!root) {return 0;}
    int length = 0;

    return dfs(root, length);
}

// Time Complexity -> O(2N) as N is the number of elements in root
// Space Complexity -> O(1) as the auxillary space remains constant
