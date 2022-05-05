#include <iostream>
using namespace std;

int main() {
    int t, n;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n;
        int sum = 0;

        for (int j = 0; j < n; j++) {
            int k;
            cin >> k;

            sum += k;
        }

        cout << sum << '\n';
    }
    return 0;
}