class Solution {
public:

    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> res;

        auto cmp = [](const vector<int>& a, const vector<int>& b) {
            return (a[0]*a[0] + a[1]*a[1]) > (b[0]*b[0] + b[1]*b[1]);
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);

        // make min heap, push all pts; pop k times and add each to res; return res

        for (auto p : points) {
            pq.push(p);
        }

        while (k > 0) {
            res.push_back(pq.top());
            pq.pop();
            --k;
        }

        return res;
    }
};