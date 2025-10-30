// Floyd's algorithm - Lptr steps 1, Rptr steps 2
// LL

// every int in the array is a pointer to the positions 0 to n in the array
// one portion is gonna form a cycle
// if two pointers point to the same node, that index is gonna be the duplicate
// we gotta find the beginning of the cycle
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];

        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) break;
        }

        // restart slow and now move both 1 step at a time
        // they are the same length away from the start of the cycle
        int slow2 = nums[0];

        while (slow != slow2) {
            slow = nums[slow];
            slow2 = nums[slow2];
        }

        return slow;
    }
};