#include <iostream>
using namespace std;

int fastFibo(int n, int arr[][2]);

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int n;
		cin >> n;
		int arr[2][2] = {{1, 1}, {1, 0}};
		cout << fastFibo(n, arr) << endl;
	}
	return 1;
}


int fastFibo(int n, int arr[][2]) {
	if (n == 0) {
		return 0;
	} else if (n == 1) {
		return 1;
	}
	else {
		fastFibo(n/2, arr);
		int a = arr[0][0]*arr[0][0] + arr[0][1]*arr[1][0];
		int b = arr[0][0]*arr[0][1] + arr[0][1]*arr[1][1];
		int c = arr[1][0]*arr[0][0] + arr[1][1]*arr[1][0];
		int d = arr[1][0]*arr[0][1] + arr[1][1]*arr[1][1];
		arr[0][0] = a % 1000;
		arr[0][1] = b % 1000;
		arr[1][0] = c % 1000;
		arr[1][1] = d % 1000;
		if (n % 2 != 0){
			int a = arr[0][0] + arr[0][1];
			int b = arr[0][0];
			int c = arr[1][0] + arr[1][1];
			int d = arr[1][0];
			arr[0][0] = a % 1000;
			arr[0][1] = b % 1000;
			arr[1][0] = c % 1000;
			arr[1][1] = d % 1000;
		}
		return arr[0][1];
	}
}
