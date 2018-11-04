// https://leetcode.com/problems/two-sum/

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        return method2(nums, target);
    }

    private int[] method1(int[] nums, int target) {
        // Runtime: O(n2), space: O(1)
        int i = 0, j = 0;
        boolean done = false;
        for (i = 0; i < nums.length - 1; i++) {
            for (j = i+1; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                if (target == nums[i] + nums[j]) {
                    done = true;
                    break;
                }
            }
            if (done) {
                break;
            }
        }

        if (done)
            return new int[] {i, j};
        return new int[] {-1, -1};
    }

    private int[] method2(int[] nums, int target) {
        // Runtime: O(n), space: O(n)
        HashMap<Integer, Integer> map = new HashMap<>();
        int diff = 0;
        for (int i = 0; i < nums.length; i++) {
            diff = target - nums[i];
            if (map.containsKey(diff)) {
                int index = map.get(diff);
                if (index == i) continue;
                return new int[] {index, i};
            }
            else {
                map.put(nums[i], i);
            }
        }
        return new int[] {-1, -1};
    }
}