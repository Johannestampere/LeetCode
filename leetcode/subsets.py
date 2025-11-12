class Solution {
public:
    vector<vector<int>> res;
    vector<int> sub;

    void dfs(int i, vector<int>& nums) {
        if (i == nums.size()) { res.push_back(sub); return; }

        sub.push_back(nums[i]);
        dfs(i + 1, nums);

        sub.pop_back();
        dfs(i + 1, nums);

    }

    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(0, nums);
        return res;
    }
};