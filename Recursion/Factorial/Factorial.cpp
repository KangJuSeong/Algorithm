#include <iostream>
using namespace std;

int factorial(int n);

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int n;
		cin >> n;
		cout << factorial(n) % 1000 << endl;
	}
	return 0;
}

int factorial(int n) {
	if (n <= 1) {
		return 1;
	} else {
		int a = n * factorial(n-1);
		while(a % 10 == 0) 
			a /= 10;
		return a % 10000;
	}
}
