#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    int H, M;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> H >> M;

        int H_angle = 60 * H + M;
        int M_angle = 12 * M;
        int angle = abs(H_angle - M_angle);

        if (angle >= 360)    angle = 720 - angle;

        cout << angle / 2 << '\n';
    }
    return 0;
}