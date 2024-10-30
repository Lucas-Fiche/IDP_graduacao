#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    for (int case_num = 0; case_num < N; ++case_num) {
        string R, S;
        cin >> R >> S;

        string T = R; 

        transform(R.begin(), R.end(), S.begin(), T.begin(),
                  [](char r, char s) {
                      if ((isupper(r) && isupper(s)) || (islower(r) && islower(s))) {
                          return toupper(r);
                      } else {
                          return tolower(r);
                      }
                  });

        cout << T << endl;
    }

    return 0;
}
