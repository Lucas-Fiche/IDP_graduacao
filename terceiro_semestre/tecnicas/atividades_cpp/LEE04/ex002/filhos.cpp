#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N, C;
    cin >> N >> C;

    vector<int> valores(N);
    for (int i = 0; i < N; i++) {
        cin >> valores[i];
    }

    vector<int> consultas(C);
    for (int i = 0; i < C; i++) {
        cin >> consultas[i];
        consultas[i]--;  
    }

    for (int consulta : consultas) {
        int esquerdo = 2 * consulta + 1;
        int direito = 2 * consulta + 2;

        string filho_esquerdo = (esquerdo < N && valores[esquerdo] != -1) ? to_string(valores[esquerdo]) : "NULL";
        string filho_direito = (direito < N && valores[direito] != -1) ? to_string(valores[direito]) : "NULL";

        cout << filho_esquerdo << " " << filho_direito << endl;
    }

    return 0;
}

// =============================================================================================================================

#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> find_children(const vector<int>& tree, int N, const vector<int>& queries) {
    vector<string> results;
    
    for (int node : queries) {
        string left_child = "NULL";
        string right_child = "NULL";
        
        if (node - 1 >= 0 && node - 1 < N && tree[node - 1] != -1) {
            for (int current_pos = 0; current_pos < N; current_pos++) {
                if (tree[current_pos] == tree[node - 1]) {
                    if (current_pos * 2 + 1 < N && tree[current_pos * 2 + 1] != -1) {
                        left_child = to_string(tree[current_pos * 2 + 1]);
                    }
                    if (current_pos * 2 + 2 < N && tree[current_pos * 2 + 2] != -1) {
                        right_child = to_string(tree[current_pos * 2 + 2]);
                    }
                    break;
                }
            }
        }
        
        results.push_back(left_child + " " + right_child);
    }
    
    return results;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, C;
    cin >> N >> C;
    
    vector<int> tree(N);
    for (int i = 0; i < N; i++) {
        cin >> tree[i];
    }
    
    vector<int> queries(C);
    for (int i = 0; i < C; i++) {
        cin >> queries[i];
    }
    
    vector<string> results = find_children(tree, N, queries);

    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}