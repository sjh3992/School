#include <iostream>
using namespace std;

int main() {
    int t, a, b, c;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> a >> b >> c;

        if (a <= b) {
            if (b <= c) {
                cout << a << ' ' << b << ' ' << c << '\n';
            }
            else if (a <= c) {
                cout << a << ' ' << c << ' ' << b << '\n';
            }
            else {
                cout << c << ' ' << a << ' ' << b << '\n';
            }
        }
        else if (c <= b) {
            cout << c << ' ' << b << ' ' << a << '\n';
        }
        else if (a <= c) {
            cout << b << ' ' << a << ' ' << c << '\n';
        }
        else {
            cout << b << ' ' << c << ' ' << a << '\n';
        }
    }
}