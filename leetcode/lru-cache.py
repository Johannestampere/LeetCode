// remove the Least Recently Used key-value pair when capacity full
// double linked list, keep track of both start and end
struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v): key{k}, val{v}, prev{nullptr}, next{nullptr} {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> cache;
    Node* head, *tail;

    void removeNode(Node* node) {
        Node* p = node->prev;
        Node* n = node->next;
        p->next = n;
        n->prev = p;
    }

    void addToFront(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }

public:
    LRUCache(int capacity): capacity{capacity} {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (!cache.count(key)) return -1;

        Node* node = cache[key];
        removeNode(node);
        addToFront(node);
        return node->val;
    }


    
    void put(int key, int value) {
        if (cache.count(key)) {
            Node* node = cache[key];
            node->val = value;
            removeNode(node);
            addToFront(node);
        } else {
            if (cache.size() == capacity) {
                Node* lru = tail->prev;
                removeNode(lru);
                cache.erase(lru->key);
                delete lru;
            }
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            addToFront(newNode);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */