#include <iostream>
using namespace std;


int main() {
	int n, k;
	cin >> n>> k;
	return 0;
}

void binoCoef(int n, int k) {
	int memo[30][30];
	int i, j;
	

	for(i=0;i<=n;i++) {
		for(j=0;j<=min(i,k); j++){
			if (j == 0 || j == i) {
				memo[i][j] = 1;
			} else {
				memo[i][j] = memo[i-1][j-1] + memo[i-1][j];
			}
		}
	}
	cout << memo[n][k];


void coeff(int n, int k) {
	int i, j;
	int m[100][100];
	for(i=0;i<=n;i++) {
		for(j=0;j<=min(i, k), j++) {
			if(j==i || j==0) {
				m[i][j] = 1;
			} else {
				m[i][j] = m[i-1][j-1] + m[i-1][j];
			}
		}
	}
}

void coin(int n, int k) {
	int i,j;
	int m[1000] = {99999};
	m[0] = 0;
	for(i=0;i<n;i++) {
		for(j=coin[i];j<=k;j++) {
			m[j] = min(m[j], m[j-coin[i]-1]);
		}
	}
	cout << m[k];
}

void coin2(int n, int k) {
	int i,j;
	int m[1000][1000] = {0};
	m[0][0] = 1;
	for(i=0;i<n;i++) {
		for(j=0;j<=k;j++) {
			if(j < coin[i]) {
				m[i][j] = m[i-1][j];
			} else {
				m[i][j] = m[i-1][j-1] + m[i-1][j];
			}
		}
	}
}