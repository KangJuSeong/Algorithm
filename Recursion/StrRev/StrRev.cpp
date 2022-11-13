#include <iostream>
#include <string>
using namespace std;

void StringReverse(string a, int idx);

int main() {
	int numTestCases;
	scanf("%d", &numTestCases);
	for (int i=0; i<numTestCases; ++i) {
		string a;
		cin >> a;
		StringReverse(a, 0);
	}
	return 1;
}

void StringReverse(string a, int idx) {
	if (idx != a.size()-1) {
		StringReverse(a, idx+1);
	}
	cout << a[idx]; 
	if (idx == 0) {
		cout << endl;
	}
}
