#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int a, b, c, d;
        int over_interval, total_interval;
        cin >> a >> b >> c >> d;

        if (a < c) {
            if (c < b && b < d) {
                over_interval = b - c;
                total_interval = d - a;
            }
            else if (b < c && c < d) {
                over_interval = 0;
                total_interval = (b - a) + (d - c);
            }
            else {
                over_interval = d - c;
                total_interval = b - a;
            }
        }
        else {
            if (a < d && d < b) {
                over_interval = d - a;
                total_interval = b - c;
            }
            else if (d < a && a < b) {
                over_interval = 0;
                total_interval = (d - c) + (b - a);
            }
            else {
                over_interval = b - a;
                total_interval = d - c;
            }
        }

        cout << over_interval << " " << total_interval << "\n";
    }
    return 0;
}