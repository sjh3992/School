#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        n /= 2;
        n -= 1;

        cout << "+";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "+";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "+\n";

        for (int i = 0; i < n; i++) {
            cout << "|";
            for (int j = 0; j < n; j++) {
                if (i == j)  cout << "\\";
                else    cout << ".";
            }
            cout << "|";
            for (int j = n - 1; j >= 0; j--) {
                if (i == j)  cout << "/";
                else    cout << ".";
            }
            cout << "|\n";
        }

        cout << "+";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "*";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "+\n";

        for (int i = n - 1; i >= 0; i--) {
            cout << "|";
            for (int j = 0; j < n; j++) {
                if (i == j)  cout << "/";
                else    cout << ".";
            }
            cout << "|";
            for (int j = n - 1; j >= 0; j--) {
                if (i == j)  cout << "\\";
                else    cout << ".";
            }
            cout << "|\n";
        }

        cout << "+";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "+";
        for (int i = 0; i < n; i++)  cout << "-";
        cout << "+\n";
    }

    return 0;
}