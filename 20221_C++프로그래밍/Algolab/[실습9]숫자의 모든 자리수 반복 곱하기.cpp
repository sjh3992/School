#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        unsigned int n, n_mul = 1;
        cin >> n;

        while (n > 0) {
            if (n % 10 != 0) {
                n_mul *= (n % 10);
            }
            n /= 10;

            if (n == 0 && n_mul > 9) {
                n = n_mul;
                n_mul = 1;
            }
        }

        cout << n_mul << "\n";
    }
    
    return 0;
}