#include <iostream>
using namespace std;

int main() {
    int t, n, k1, k2;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n >> k1;

        for (int j = 1; j < n; j++) {
            cin >> k2;

            k1 = k1 % 10;
            k2 = k2 % 10;
            k1 = k1 * k2;
            k1 = k1 % 10;
        }

        cout << k1 % 10 << '\n';
    }
    return 0;
}