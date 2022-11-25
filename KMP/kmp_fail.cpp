#include <iostream>
using namespace std;

int cnt;
int fail[1000] = {0,};
int fail_func(int n, string s);
int KMP(string s1, string s2);

int main() {
	int numTestCases, i, j;
	cin >> numTestCases;
	for(i=0;i<numTestCases;i++) {
		string s1, s2;
		cin >> s1 >> s2;
		cnt = 0;
		for(j=0;j<s1.length();j++) {
			cout << fail_func(j, s1) << " ";
		}
		cout << endl;
		cout << KMP(s2, s1) << endl;
		for(j=0;j<1000;j++) { fail[j] = 0; }
	}
}


int fail_func(int n, string s) {
	int j = 0;
	int i;
	for(i=1;i<s.length();i++) {
		while (j > 0 && s[i] != s[j]) { 
			j = fail[j-1];
		}
		if (s[i] == s[j]) {
			fail[i] = ++j;
		}
	}
	return fail[n];
}

int KMP(string s1, string s2) {
	int j=0;
	int i;
	for(i=0;i<s1.length();i++) {
		while (j>0 && s1[i] != s2[j]) {
			j = fail[j-1];
		}
		if(s1[i] == s2[j]) {
			if(j == s2.length()-1) {
				cnt ++;
				j = fail[j];
			} else {
				j++;
			}
		}
	}
	return cnt;
}

