#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    cin.ignore();

    vector<string> resultados;
    resultados.reserve(n);
    
    while (n--) {
        string str1, str2;
        cin >> str1 >> str2;

        if (str1.size() != str2.size()) {
            resultados.push_back("DIFERENTES");
            continue;
        }

        int freq[128] = {0};

        for (size_t i = 0; i < str1.size(); ++i) {
            freq[static_cast<int>(str1[i])]++;
            freq[static_cast<int>(str2[i])]--;
        }

        bool anagrama = true;
        for (int i = 0; i < 128; ++i) {
            if (freq[i] != 0) {
                anagrama = false;
                break;
            }
        }

        resultados.push_back(anagrama ? "ANAGRAMAS" : "DIFERENTES");
    }

    for (const auto& res : resultados) {
        cout << res << '\n';
    }

    return 0;
}
