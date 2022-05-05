#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, S = 0;
        cin >> n;
        string n_string = to_string(n);
        int k = n_string.length();

        for (int j = 0; j < k; j++) {
            int temp = n;
            temp /= (int)pow(10, j);
            S += (int)pow(temp % 10, k);
        }

        if (S == n)  cout << "1\n";
        else         cout << "0\n";
    }

    return 0;
}