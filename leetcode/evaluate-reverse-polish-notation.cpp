#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stack;

        for (string& c : tokens) {
            if (c == "+" || c == "*" || c == "-" || c == "/") {

                int a = stack.back();
                stack.pop_back();
                int b = stack.back();
                stack.pop_back();

                if (c == "+") {
                    stack.push_back(a + b);
                } else if (c == "*") {
                    stack.push_back(a * b);
                } else if (c == "-") {
                    stack.push_back(b - a);
                } else {
                    stack.push_back(b / a);
                }
            }
            else {
                stack.push_back(stoi(c));
            }
        }

        return stack.back();
    }
};