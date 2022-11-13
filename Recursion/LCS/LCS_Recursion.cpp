#include <iostream>
using namespace std;


int LCS(string s, string t, int m, int n);

int main(){
	int numTestCase = 0;
	cin >> numTestCase;	
	for(int k=0;k<numTestCase;k++) {
		string s, t;
		cin >> s >> t;
		int m = s.size();
		int n = t.size();
		cout << LCS(s, t, m, n) << endl;
	}
	return 0;
}

int LCS(string s, string t, int m, int n) {
	if (m == 0 || n == 0) return 0;
	else if(s[m-1] == t[n-1]) return LCS(s, t, m-1, n-1) + 1;
	else {
		return max(LCS(s, t, m, n-1), LCS(s, t, m-1, n));
	}
}

