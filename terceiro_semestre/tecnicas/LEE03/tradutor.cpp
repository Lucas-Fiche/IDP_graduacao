#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool isBalanced(string s) {
    stack<char> parentheses;
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            parentheses.push(c);
        } else if (c == ')' || c == '}' || c == ']') {
            if (parentheses.empty()) return false;
            char top = parentheses.top();
            parentheses.pop();
            if ((c == ')' && top != '(') || 
                (c == '}' && top != '{') || 
                (c == ']' && top != '[')) {
                return false;
            }
        }
    }
    return parentheses.empty();
}

int main() {
    string s;
    cin >> s;

    if (isBalanced(s)) {
        cout << "OK" << endl;
    } else {
        cout << "SyntaxError" << endl;
    }

    return 0;
}
