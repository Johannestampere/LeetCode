class Solution {
public:
    int max(int a, int b) {
        if (a >= b) return a;
        else return b;
    }

    int maxProfit(vector<int>& prices) {
        int L = 0;
        int R = 1;

        int res = 0;

        while (R < prices.size()) {
            if (prices[R] - prices[L] < 0) {
                L = R;
                continue;
            } 

            else {
                res = max(res, prices[R] - prices[L]);
                ++R;
            }
        }

        return res;
    }
};
