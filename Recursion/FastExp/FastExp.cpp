#include <iostream>
using namespace std;

int fastExp(int a, int b);

int main(){
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int a, b;
		cin >> a >> b;
		cout << fastExp(a, b) << endl;
	}
	return 1;
}

int fastExp(int a, int b) {
	if (b == 0) return 1;
	else if(b % 2 == 1){
		int y = fastExp(a, (b-1)/2);
		return a * y * y % 1000;
	} else {
		int y = fastExp(a, b/2);
		return y * y % 1000;
	}
}


