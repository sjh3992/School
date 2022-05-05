#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, stock[1000] = { 0, };
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> stock[i];
        }

        int left = stock[0];
        int now = stock[1];
        int right = stock[2];
        int count = 0;

        for (int i = 1; i < n - 1; i++) {
            if (now == right) {
                right = stock[i + 2];
                continue;
            }

            if (left < now && now > right) {
                count++;
            }

            left = stock[i];
            now = stock[i + 1];
            right = stock[i + 2];
        }
        cout << count << "\n";
    }
    return 0;
}