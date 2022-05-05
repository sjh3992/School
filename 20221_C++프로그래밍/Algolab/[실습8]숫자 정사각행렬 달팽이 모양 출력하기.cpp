#include <iostream>
using namespace std;
int arr[1000][1000];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, a, b, num = 1;
        cin >> n >> a >> b;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = num++;
            }
        }

        num = 1;
        int st = 0;
        for (; n > 0; n -= 2, st++) {
            int last = st + n - 1;

            for (int i = st; i < last + 1; i++) {
                if (a <= num && num <= b) {
                    cout << arr[st][i] << " ";
                }
                num++;
            }

            for (int i = st + 1; i < last + 1; i++) {
                if (a <= num && num <= b) {
                    cout << arr[i][last] << " ";
                }
                num++;
            }

            for (int i = last - 1; i > st - 1; i--) {
                if (a <= num && num <= b) {
                    cout << arr[last][i] << " ";
                }
                num++;
            }

            for (int i = last - 1; i > st; i--) {
                if (a <= num && num <= b) {
                    cout << arr[i][st] << " ";
                }
                num++;
            }
        }

        cout << "\n";
    }

    return 0;
}