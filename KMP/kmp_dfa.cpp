#include <iostream>
using namespace std;

int state_table[3][1001] = {0, };
char state_char[3] = {'A', 'B', 'C'};
void dfa(string s);
int is_suffix(string s1, string s2);
int cnt;
int no_zero;
void string_matching(string s1, int n);


int main() {
	int numTestCases, i;
	cin >> numTestCases;
	for(i=0;i<numTestCases;i++) {
		string s1, s2;
		cin >> s1 >> s2;
		cnt = 0;
		no_zero = 0;
		dfa(s1);
 //		for(int k=0;k<3;k++) {
 //			for(int j=0; j<s1.length()+1;j++) {
 //				cout << state_table[k][j] << " ";
 //			}
 //			cout << endl;
 //		}
		string_matching(s2, s1.length());	
		cout << no_zero << " " << cnt << endl;
	}
	return 0;
}


int is_suffix(string s1, string s2) {
	int i, j;
	int p = s1.length();
	int s = s2.length();
	if(p > s) return 0;
	for(i=p-1,j=s-1; i>=0; i--,j--){
		if(s1[i] != s2[j]) return 0;
	}
	return 1;
}


void dfa(string s) {
	int state = 0;
	int i, j;
	for(state=0; state<s.length()+1; state++) {
		for(i=0; i<3; i++) {
			string k = s.substr(0, state);
			k += state_char[i];
			string m = s.substr(0, state+1);
			j = m.length();
			while(!is_suffix(m, k)) {
				j --;
				m = s.substr(0, j);
			}
			state_table[i][state] = j;
			if(j!=0) no_zero ++;
		}
	}
}


void string_matching(string s1, int n) {
	int i,j;
	int state = 0;
	for(i=0;i<s1.length();i++) {
		if (s1[i] == state_char[0]) j=0;
		if (s1[i] == state_char[1]) j=1;
		if (s1[i] == state_char[2]) j=2;
		state = state_table[j][state];	
		if(state==n) cnt ++;
	}
}
