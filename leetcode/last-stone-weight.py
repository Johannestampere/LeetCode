// MAX HEAP: binary tree where root is always the max element
// push() - O(logn) : 1)new e is placed in end of array 2)the e is bubbled up (max H times, so log2n => logn)
// top() - O(1) : root access
// pop() - same logic as push, max log2n times => logn
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, less<int>> pq; // max heap

        for (int stone : stones) {
            pq.push(stone);
        }

        while (pq.size() > 1) {
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();

            if (x == y) { continue; }
            else {
                pq.push(x-y);
            }
        }

        if (pq.size() == 1) return pq.top();
        return 0;
    }
};