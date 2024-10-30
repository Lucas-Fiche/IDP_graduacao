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
        if (consulta == 0) {
            cout << "RAIZ" << endl;
        } else {
            int pai_index = (consulta - 1) / 2;
            if (pai_index >= 0 && valores[pai_index] != -1) {
                cout << valores[pai_index] << endl;
            } else {
                cout << "NULL" << endl;
            }
        }
    }

    return 0;
}

// ==============================================================================

#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> find_parent(const vector<int>& tree, int N, const vector<int>& queries) {
    vector<string> results;
    
    for (int node : queries) {
        if (node - 1 >= N || node - 1 < 0 || tree[node - 1] == -1) {
            results.push_back("NULL");
            continue;
        }
        
        if (node - 1 == 0) {
            results.push_back("RAIZ");
            continue;
        }
        
        string parent_value = "NULL";
        for (int i = 0; i < N; i++) {
            if (tree[i] != -1) {  
                int left_child_idx = 2 * i + 1;
                int right_child_idx = 2 * i + 2;
                
                if ((left_child_idx < N && tree[left_child_idx] == tree[node - 1]) || 
                    (right_child_idx < N && tree[right_child_idx] == tree[node - 1])) {
                    parent_value = to_string(tree[i]);
                    break;
                }
            }
        }
        
        results.push_back(parent_value);
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
    
    vector<string> results = find_parent(tree, N, queries);
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}