#include <iostream>
using namespace std;

int min(int a, int b) {
    if (a >= b) return b;
    else return a;
}

int fn(int coin, int k, int cnt) {
    if(k==0) return cnt;
    else if(k < 0) {
        return 9999999;
    }
    else {
        return fn(coin, k-coin, cnt+1);
    }
}

void test(int coin[], int n, int k) {
    int a = 999999;
    for (int i=0;i<n;i++) {
        a = min(fn(coin[i], k, a), a);
    }
	cout << a << endl;
}

int main() {
    int m;
    cin >> m;
    for(int i=0;i<m;i++) {
        int k;
        cin >> k; 
        int n;
        cin >> n;
        int coin[n];
        for(int j=0;j<n;j++) {
            cin >> coin[j];
        }
        test(coin, n, k);
    }
    return 0;
}
