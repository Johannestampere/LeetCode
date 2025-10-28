class Solution {
public:

    vector<string> res;
    string cur;

    void backtrack(int openN, int closedN, int n) {
        // if cur string is valid
        if (openN == n && closedN == n) {
            res.push_back(cur);
            return;
        }

        // add open
        if (openN < n) {
            cur.push_back('(');
            backtrack(openN + 1, closedN, n);
            cur.pop_back();
        }

        // add closed
        if (closedN < openN) {
            cur.push_back(')');
            backtrack(openN, closedN + 1, n);
            cur.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        // only add open paren. when open count < n
        // only add closed when closed count < open
        // valid if open == closed == n

        backtrack(0, 0, n);
        return res;
    }
};