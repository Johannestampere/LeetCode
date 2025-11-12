class Solution {
public:
    vector<vector<int>> res;
    void backtrack(int i, vector<int> sub, vector<int>& nums) {
        if (i == nums.size()) { res.push_back(sub); return; }

        // all subsets that include nums[i]
        sub.push_back(nums[i]);
        backtrack(i+1, sub, nums);
        sub.pop_back();

        // all subsets that dont include nums[i]
        while (i + 1 < nums.size() && nums[i] == nums[i+1]) {
            ++i;
        }   
        backtrack(i+1, sub, nums);

    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> sub;

        backtrack(0, sub, nums);

        return res;
    }
};