#include <bits/stdc++.h>
using namespace std;

bool compare(const string &a, const string &b) {
    if (a.size() != b.size())
        return a.size() < b.size();  
    return a < b;  
}

int main() {
    int N;
    cin >> N;

    vector<string> livros(N);

    for (int i = 0; i < N; i++) {
        cin >> livros[i];
    }

    sort(livros.begin(), livros.end(), compare);

    for (const string &livro : livros) {
        cout << livro << endl;
    }

    return 0;
}
