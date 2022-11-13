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
				memo[i][j] = 0;
			}
		}
		cout << LCS(s, t, m, n) << endl;
	}
	return 0;
}

int LCS(string s, string t, int m, int n) {
	int i,j;
	for(i=1;i<=m;i++) {
		for(j=1;j<=n;j++) {
			if (s[i-1] == t[j-1]){
				L[i][j] = L[i-1][j-1] + 1;
				S[i][j] = 0;
			} else {
				L[i][j] = max(L[i][j-1], L[i-1][j]);
				if (L[i][j] == L[i][j-1]) S[i][j] = 1;
				else S[i][j] = 2;
			}
		}
	}
	return L[m][n];
}

