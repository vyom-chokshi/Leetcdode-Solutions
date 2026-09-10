/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int count=0;

    int[] dfs(TreeNode node)
        {
            if(node==null)
            return new int[]{0,0};

            int[] lft=dfs(node.left);
            int[] rgh=dfs(node.right);

            int sum=node.val+lft[0]+rgh[0];
            int c=1+lft[1]+rgh[1];

            if(sum/c==node.val)
            {
                count++;
            }
            return new int[]{sum,c};
        }

    public int averageOfSubtree(TreeNode root) 
    {
        
        dfs(root);
        return count;
    }
}