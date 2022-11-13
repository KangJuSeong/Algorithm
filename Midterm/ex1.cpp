#include <iostream>
using namespace std;

int min(int a, int b) {
    if (a >= b) return b;
    else return a;
}

void fn(int n, int k) {
    int i,j;
    int memo[1000][1000] = {0};
    for(i=0;i<=n;i++) {
        for(j=0;j<=n;j++) {
            if(i==j || j==0) {
                memo[i][j] = 1;
            } else {
                memo[i][j] = (memo[i-1][j-1] + memo[i-1][j]) % 1000;
            }
        }
    }
    cout << memo[n][k] % 1000 << endl;
}

int main() {
    int testcase;
    cin >> testcase;
    for(int i=0;i<testcase;i++) {
        int n, k;
        cin >> n >> k;
        fn(n, k);
    }
    return 0;
}