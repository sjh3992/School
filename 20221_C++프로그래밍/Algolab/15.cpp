// 변수 이름
// 소프트웨어학부 20213009 서지훈

#include <iostream>
#include <string>
using namespace std;

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    while(t--) {
        string var;
        bool flag = true;
        cin >> var;
        
        for(int i = 0; i < var.size(); i++) {
            if('a' <= var[i] && var[i] <= 'z')  continue;
            else if('A' <= var[i] && var[i] <= 'Z') continue;
            else if('0' <= var[i] && var[i] <= '9' && i) continue;
            else if(var[i] == '_')  continue;
            else {
                flag = false;
                cout << "0\n";
                break;
            }
        }

        if(flag)    cout << "1\n";
    }

    return 0;
}