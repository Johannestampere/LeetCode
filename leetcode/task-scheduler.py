class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        priority_queue<int> maxHeap;

        for (char t : tasks) {
            freq[t]++;
        }

        for (auto& p : freq) {
            maxHeap.push(p.second);
        }

        queue<pair<int, int>> q;   // {remaining_count, time_when_available}

        int time = 0; // track global time

        while (!maxHeap.empty() || !q.empty()) {
            time++;

            if (!maxHeap.empty()) {
                int count = maxHeap.top();
                maxHeap.pop();

                --count;

                if (count > 0) {
                    q.push({count, time + n});
                }
            }

            if (!q.empty() && q.front().second == time) {
                maxHeap.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};