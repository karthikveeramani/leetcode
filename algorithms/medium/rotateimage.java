// https://leetcode.com/problems/rotate-image/

class Solution {
    // Runtime: O(n2), Space: O(1)
    public void rotate(int[][] matrix) {
        transpose(matrix);
        reorderColumns(matrix);
    }

    private void print(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("[");
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.print("] ");
        }
    }

    private void transpose(int[][] matrix) {
        int temp = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                if (i >= j) continue;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    private void reorderColumns(int[][] matrix) {
        int temp = 0;
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n/2; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
}