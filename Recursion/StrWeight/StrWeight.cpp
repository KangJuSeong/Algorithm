#include <iostream>
using namespace std;

void swap(char* a, char* b);
int calWeight(string &a, int len);
void permutation(string &a, int idx, int len);
int pow(int a, int b);
int cnt;

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		string a;
		cin >> a;
		cnt = 0;
		permutation(a, 0, a.length());
		cout << cnt << endl;
	}
	return 1;
}

int calWeight(string &a, int len) {
	int weight = 0;
	for (int i=0; i<len; i++) {
		weight += pow(-1, i) * (int(a[i])-int('a'));
	}
	return weight;
}

int pow(int a, int b) {
	int c = 1;
	for(int i=0; i<b; i++) {
		c *= a;
	}
	return c;
}

void swap(char* a, char* b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void permutation(string &a, int idx, int len) {
	if (idx == len - 1) {
		if (calWeight(a, len) > 0) { cnt ++; }
		return ;
	} 
	for (int j=idx; j<len; j++) {
		swap(&a[idx], &a[j]);
		permutation(a, idx + 1, len);
		swap(&a[idx], &a[j]);
	}
}
