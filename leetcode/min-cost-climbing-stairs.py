class Solution {
public:

    // each step i has a cost[i] to stand on it
    // to reach step i, we could have gone from
    //      1) step (i-1), paying cost[i-1]
    //      2) step (i-2), paying cost[i-2]
    // min_cost[i]=min(min_cost[i−1]+cost[i−1],min_cost[i−2]+cost[i−2])


    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        vector<int> min_cost = {0, 0};

        for (int i = 2; i < n + 1; ++i) {
            int next_cost = min(min_cost[i-2] + cost[i-2], min_cost[i-1] + cost[i-1]);

            min_cost.push_back(next_cost);
        }

        return min_cost.back();
    }
};