#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
public:
    Node* root;
    BinarySearchTree() : root(nullptr) {}

    void insert(int key) {
        root = insert_recursive(root, key);
    }

    void inorder(Node* node, vector<int>& result) {
        if (node) {
            inorder(node->left, result);
            result.push_back(node->value);
            inorder(node->right, result);
        }
    }

    void preorder(Node* node, vector<int>& result) {
        if (node) {
            result.push_back(node->value);
            preorder(node->left, result);
            preorder(node->right, result);
        }
    }

    void postorder(Node* node, vector<int>& result) {
        if (node) {
            postorder(node->left, result);
            postorder(node->right, result);
            result.push_back(node->value);
        }
    }

private:
    Node* insert_recursive(Node* node, int key) {
        if (!node) return new Node(key);
        if (key < node->value)
            node->left = insert_recursive(node->left, key);
        else
            node->right = insert_recursive(node->right, key);
        return node;
    }
};

int main() {
    int N;
    cin >> N;

    BinarySearchTree bst;
    for (int i = 0; i < N; ++i) {
        int value;
        cin >> value;
        bst.insert(value);
    }

    vector<int> inorder_result;
    bst.inorder(bst.root, inorder_result);
    cout << "In: ";
    for (int val : inorder_result) cout << val << " ";
    cout << endl;

    vector<int> preorder_result;
    bst.preorder(bst.root, preorder_result);
    cout << "Pre: ";
    for (int val : preorder_result) cout << val << " ";
    cout << endl;

    vector<int> postorder_result;
    bst.postorder(bst.root, postorder_result);
    cout << "Pos: ";
    for (int val : postorder_result) cout << val << " ";
    cout << endl;

    return 0;
}

// ========================================================================

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Node {
public:
    int value;
    Node* left;
    Node* right;
    
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BST {
private:
    Node* root;
    
    void _insert_recursive(Node* node, int value) {
        if (value <= node->value) {
            if (node->left == nullptr) {
                node->left = new Node(value);
            } else {
                _insert_recursive(node->left, value);
            }
        } else {
            if (node->right == nullptr) {
                node->right = new Node(value);
            } else {
                _insert_recursive(node->right, value);
            }
        }
    }
    
    void _inorder_recursive(Node* node, vector<int>& result) {
        if (node) {
            _inorder_recursive(node->left, result);
            result.push_back(node->value);
            _inorder_recursive(node->right, result);
        }
    }
    
    void _preorder_recursive(Node* node, vector<int>& result) {
        if (node) {
            result.push_back(node->value);
            _preorder_recursive(node->left, result);
            _preorder_recursive(node->right, result);
        }
    }
    
    void _postorder_recursive(Node* node, vector<int>& result) {
        if (node) {
            _postorder_recursive(node->left, result);
            _postorder_recursive(node->right, result);
            result.push_back(node->value);
        }
    }
    
    void _cleanup(Node* node) {
        if (node) {
            _cleanup(node->left);
            _cleanup(node->right);
            delete node;
        }
    }
    
public:
    BST() : root(nullptr) {}
    
    ~BST() {
        _cleanup(root);
    }
    
    void insert(int value) {
        if (!root) {
            root = new Node(value);
        } else {
            _insert_recursive(root, value);
        }
    }
    
    vector<int> inorder() {
        vector<int> result;
        _inorder_recursive(root, result);
        return result;
    }
    
    vector<int> preorder() {
        vector<int> result;
        _preorder_recursive(root, result);
        return result;
    }
    
    vector<int> postorder() {
        vector<int> result;
        _postorder_recursive(root, result);
        return result;
    }
};

void print_vector(const vector<int>& vec, const string& prefix) {
    cout << prefix;
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i < vec.size() - 1) cout << " ";
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    
    BST bst;
    for (int i = 0; i < N; i++) {
        int value;
        cin >> value;
        bst.insert(value);
    }
    
    print_vector(bst.inorder(), "In.: ");
    print_vector(bst.preorder(), "Pre: ");
    print_vector(bst.postorder(), "Pos: ");
    
    return 0;
}