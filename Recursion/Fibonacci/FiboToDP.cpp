#include <iostream>
using namespace std;

int memo[100];
int fibo(int n);

int main() {
	for (int i=0; i<100; i++) {
		memo[i] = -1;
	}
	cout << fibo(100);
	return 0;
}

int fibo(int n) {
	memo[0] = 0;
	memo[1] = 1;

	for(int i=2; i<=n;i++) {
		memo[i] = memo[i-1] + memo[i-2];
	}
	for(int i=0; i<100; i++) {
		cout << memo[i] << endl;
	}
	return memo[1];
}
