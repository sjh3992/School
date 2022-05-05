#include <iostream>
using namespace std;

bool leap_year(int Y) {
    if(Y % 400 == 0)    return true;
    else if(Y % 100 == 0)   return false;
    else if(Y % 4 == 0) return true;
    else    return false;
}

int main() {
    int t;
    const int month[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    cin >> t;

    while(t--) {
        int Y, M, D;
        int day = 0;
        cin >> Y >> M >> D;

        for(int i = 1; i < Y; i++) {
            if(leap_year(i))    day += 366;
            else    day += 365;
        }
        
        for(int i = 1; i < M; i++) {
            if(i == 2 && leap_year(Y))  day += 29;
            else    day += month[i];
        }

        day += D;

        cout << day % 7 << "\n";
    }

    return 0;
}