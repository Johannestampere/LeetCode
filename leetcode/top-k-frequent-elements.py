class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map; // number: count

        // add all nums and relative counts to map, O(n)
        for (int i = 0; i < nums.size(); ++i) {
            if (map.count(nums[i])) {
                ++map[nums[i]];
            } else {
                map[nums[i]] = 1;
            }
        }

        vector<vector<int>> bucket(nums.size() + 1);

        // iter thru all keys and add them to their count bucket
        for (auto pair : map) {
            bucket[pair.second].push_back(pair.first);
        }

        vector<int> res;

        for (int i = bucket.size() - 1; i >= 0 && res.size() < k; --i){
            for (int j = 0; j < bucket[i].size(); ++j) {
                if (res.size() == k) {
                    return res;
                }
                res.push_back(bucket[i][j]);
            }
        }

        return res;
    }
};