/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/*
Recursively checks the height for a balanced
binary tree. It utilizes the '-1' return key
to identify the false boolean.
*/
int checkHeight(struct TreeNode* root) {

    if (!root) {return 0;}

    int leftHeight = checkHeight(root->left);
    if (leftHeight == -1) {return -1;}
    int rightHeight = checkHeight(root->right);
    if (rightHeight == -1) {return -1;}

    if (abs(leftHeight - rightHeight) > 1) {return -1;}
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}


bool isBalanced(struct TreeNode* root) {
    return checkHeight(root) != -1;
}

// Time Complexity -> O(2N) as N is the number of elements in root
// Space Complexity -> O(1) as the auxillary space remains constant
