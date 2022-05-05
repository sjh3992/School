#include <iostream>
#include <climits>
using namespace std;

int main() {
    int t, n, k;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int min = INT_MAX;
        int max = INT_MIN;
        cin >> n;

        for (int j = 0; j < n; j++) {
            cin >> k;
            if (k > max)  max = k;
            if (k < min) min = k;
        }

        cout << max << ' ' << min << '\n';
    }
    return 0;
}