#include <iostream>
using namespace std;


int memo[101][101];

int LCS(string s, string t, int m, int n);

int main(){
	int numTestCase = 0;
	cin >> numTestCase;	
	for(int k=0;k<numTestCase;k++) {
		string s, t;
		cin >> s >> t;
		int m = s.size();
		int n = t.size();
		int i, j;
		for(i=0;i<=m;i++) {
			for(j=0;j<=n;j++){
				memo[i][j] = -1;
			}
		}
		cout << LCS(s, t, m, n) << endl;
	}
	return 0;
}

int LCS(string s, string t, int m, int n) {
	if (m == 0 || n == 0) return 0;
	if (memo[m-1][n-1] != -1) return memo[m-1][n-1];
	if (s[m-1] == t[n-1]) {
		memo[m-1][n-1] = LCS(s, t, m-1, n-1) + 1;
		return memo[m-1][n-1];
	} else {
		memo[m-1][n-1] = max(LCS(s, t, m, n-1), LCS(s, t, m-1, n));
		return memo[m-1][n-1];
	}
}

