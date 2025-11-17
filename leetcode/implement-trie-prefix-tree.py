struct TrieNode {
    // one for each letter, if nullptr => not a child
    vector<TrieNode*> children;
    bool end;

    TrieNode() : children(26, nullptr), end(false) {}

    ~TrieNode() {
        for (auto child : children) {
            delete child;
        }
    }
};

class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }

    ~Trie() { delete root; }
    
    void insert(string word) {
        TrieNode* cur = root;
        for (auto c : word) {
            // if the char doesnt exist, create it and move
            if (!cur->children[c - 'a']) {
                cur->children[c - 'a'] = new TrieNode();
            }
            cur = cur->children[c - 'a'];
        }
        cur->end = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        for (auto c : word) {
            if (!cur->children[c - 'a']) {
                return false;
            }
            cur = cur->children[c - 'a'];
        }
        if (cur->end == true) { return true; }
        else { return false; }
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
        for (char c : prefix) {
            if (!cur->children[c - 'a']) return false;
            cur = cur->children[c - 'a'];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */