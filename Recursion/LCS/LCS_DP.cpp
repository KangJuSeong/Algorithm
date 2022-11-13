#include <iostream>
using namespace std;


int L[101][101];
int S[101][101];

int LCS(string s, string t, int m, int n);
void printLCS(string s, string t, int m, int n);

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
				if (j==0) L[i][0] = 0;
				if (i==0) L[0][j] = 0;
			}
		}
		cout << LCS(s, t, m, n) << " ";
		printLCS(s, t, m, n);
		cout << endl;
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

void printLCS(string s, string t, int m, int n) {
	if (m==0 || n==0) return;
	if (S[m][n] == 0) {
		printLCS(s, t, m-1, n-1);
		cout << s[m-1];
	} else if(S[m][n] == 1) {
		printLCS(s, t, m, n-1);
	} else if(S[m][n] == 2) {
		printLCS(s, t, m-1, n);
	}
}
