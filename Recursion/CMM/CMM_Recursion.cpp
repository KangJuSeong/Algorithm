#include <iostream>
using namespace std;

int matrix[101];

int CMM(int m, int n, int matrix[]);

int main() {
	int numTestCase;
	cin >> numTestCase;
	for(int i=0;i<numTestCase;i++) {
		int n;
		cin >> n;
		for(int j=0;j<=n;j++) cin >> matrix[j];	
		cout << CMM(1, n, matrix) << endl;
	}
	return 0;
}

int CMM(int m, int n, int matrix[]) {
	int i, v, t;
	if (m == n) return 0;
	v = 987654321;

	for(i=m;i<n;i++) {
		t = CMM(m, i, matrix) + CMM(i+1, n, matrix) + (matrix[m-1]*matrix[i]*matrix[n]);
		v = min(v, t);
	}
	return v;
}

