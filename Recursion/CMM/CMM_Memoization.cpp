#include <iostream>
using namespace std;

int memo[101][101];
int matrix[102];

int CMM(int m, int n, int matrix[]);

int main() {
	int numTestCase;
	cin >> numTestCase;
	for(int i=0;i<numTestCase;i++) {
		int n;
		cin >> n;
		for(int j=0;j<=n;j++) cin >> matrix[j];	
		for(int k=0;k<=n;k++) {
			for(int l=0;l<=n;l++) {
				memo[k][l] = -1;
			}
		}
		cout << CMM(1, n, matrix) << endl;
	}
	return 0;
}

int CMM(int m, int n, int matrix[]) {
	if (m == n) return 0;
	if (memo[m][n] != -1) return memo[m][n];
	memo[m][n] = 987654321;
	for(int i=m;i<n;i++) {
		memo[m][n] = min(memo[m][n], CMM(m, i, matrix) + CMM(i+1, n, matrix) + matrix[m-1]*matrix[i]*matrix[n]);
	}
	return memo[m][n];
}

