#include <iostream>
using namespace std;

int o[101][101];
int dp[101][101];
int matrix[102];

void CMM(int n);
void order(int a, int b);

int main() {
	int numTestCase;
	cin >> numTestCase;
	for(int i=0;i<numTestCase;i++) {
		int n;
		cin >> n;
		for(int j=0;j<=n;j++) cin >> matrix[j];	
		CMM(n+1);
		order(1, n);
		cout << endl;
		cout << dp[1][n] << endl;
	}
	return 0;
}

void CMM(int n) {
	int i,j,k;
	for(i=0;i<n;i++) {
		for(j=0;j<n-i;j++){
			int m = i + j;
			if(m == j) dp[j][m] = 0;
			else {
				dp[j][m] = 987654321;
				for(k=j;k<m;k++) {
					if (dp[j][m] > (dp[j][k] + dp[k+1][m]) + (matrix[j-1]*matrix[k]*matrix[m])) {
						o[j][m] = k;
					}
					dp[j][m] = min(dp[j][m], (dp[j][k]+dp[k+1][m]) + (matrix[j-1]*matrix[k]*matrix[m]));
				}
			}
		}
	}
}

void order(int a, int b) {
	if (a == b) cout << "M" << a;
	else {
		int c = o[a][b];
		cout << "(";
		order(a, c);
		order(c+1, b);
		cout << ")";
	}
}
