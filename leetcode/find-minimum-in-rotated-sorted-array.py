class Solution {
public:
    int findMin(vector<int>& nums) {
        int L = 0;
        int R = nums.size() - 1;
        while (L < R) {
            int m = (L + R) / 2;
            if (nums[m] > nums[R]) {
                L = m + 1;
            }
            else {
                R = m;
            }
        }

        return nums[L];
    }
};