/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/


class Solution {
// two iterations:
// 1 - make deep copies of all the nodes, and make a hashmap with keys being
//     the original node ptrs and vals being ptrs to the new nodes
// 2 - connect both the nexts and randoms using hashmap
// return head's value in hashmap
public:
    unordered_map<Node*, Node*> hash;

    Node* copyRandomList(Node* head) {
        Node* cur = head; 

        // 1st iter
        while (cur) {
            hash[cur] = new Node(cur->val);
            cur = cur->next;
        }

        // 2nd iter
        cur = head;
        while (cur) {
            hash[cur]->next = hash[cur->next];
            hash[cur]->random = hash[cur->random];
            cur = cur->next;
        }

        return hash[head];
    }
};