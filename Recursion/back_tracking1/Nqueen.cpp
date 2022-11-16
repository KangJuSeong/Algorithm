#include <iostream>
using namespace std;


int board[16];
int nqueen(int row, int size, int cnt);


int main() {
	int numTestCases, i, j, k;
	cin >> numTestCases;
	for(i=0;i<numTestCases;i++) {
		int n;
		cin >> n;
		for(j=0;j<n;j++) {board[j] = -1;}
		for(k=0;k<n;k++) {
			board[0] = k;
			if(nqueen(1, n, 1)) {
				break;
			} else {
				board[0] = -1;
			}
		}
		for(j=0;j<n;j++) {
			cout << board[j]+1 << " ";
		}
		cout << endl;
	}
	return 0;
}

int nqueen(int row, int size, int cnt) {
	if (row == size) {
		return 1;
	}
	int col;
	for(col=0;col<size;col++) {
		int check = 1;
		int j = 0;
		while(j < row) {
			int k = row - j;
			if (board[j] == col || board[j]-k==col || board[j]+k==col) {
				check = 0;
				break;
			}
			j++;
		}
		if (check) {
			board[row] = col;
			if(nqueen(row+1, size, cnt++)) {
				return 1;
			} else {
				board[row] = -1;
			}
		}
	}
	return 0;
}

