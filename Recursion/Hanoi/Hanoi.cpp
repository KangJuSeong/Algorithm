#include <iostream>
using namespace std;


void hanoi(int n, int a, int b, int c);
void movePrint(int n, int a, int b);
int top;
int *pin;
int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int n;
		cin >> n;
		top = -1;
		pin = new int[n];
		hanoi(n, 1, 2, 3);
		cout << endl;
	}
	return 1;
}


void movePrint(int n, int a,int b){
	if (a == 3) {
		top --;
		if (top < 0) {
			cout << "0 ";
		} else {
			cout << pin[top] << " ";
		}
	} else if (b == 3) {
		cout << n << " ";
		top ++;
		pin[top] = n;
	} 
}

void hanoi(int n,int a,int b,int c){
    if(n == 1){
        movePrint(n, a, c);
    }
    else{
        hanoi(n-1, a, c, b);
        movePrint(n, a, c);
        hanoi(n-1, b, a, c);
    }
}


