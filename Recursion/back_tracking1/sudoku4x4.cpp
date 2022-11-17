#include <iostream>
using namespace std;


int arr[4][4];
int row[4][5];
int col[4][5];
int squ[4][5];
int flag;
void sudoku(int n);


int main(){
	int numTestCases, i, j, k;
	cin >> numTestCases;
	for(i=0;i<numTestCases;i++) {
		flag = 0;
		for(j=0;j<4;j++) {
			for(k=0;k<5;k++) {
				row[j][k] = 0;
				col[j][k] = 0;
				squ[j][k] = 0;
			}
		}
		for(j=0;j<4;j++) {
			for(k=0;k<4;k++) {
				cin >> arr[j][k];
				if(arr[j][k] != 0) {
					row[j][arr[j][k]] = 1;
					col[k][arr[j][k]] = 1;
					squ[j/2*2+k/2][arr[j][k]] = 1;
				}
			}
		}
		sudoku(0);	
	}
	return 0;
}

void sudoku(int n) {
	if (n == 16 && flag == 0) {
		int j, k;
		for(j=0;j<4;j++) {
			for(k=0;k<4;k++) {
				cout << arr[j][k] << " ";
			}
			cout << endl;
		}
		flag = 1;
		return;
	}
	int i;
	int x = n / 4;
	int y = n % 4;
	if (arr[x][y] == 0) {
		for(i=1;i<=4;i++) {
			if(row[x][i] != 1 && col[y][i] != 1 && squ[x/2*2+y/2][i] != 1) {
				row[x][i] = 1;
				col[y][i] = 1;
				squ[x/2*2+y/2][i] = 1;
				arr[x][y] = i;
				sudoku(n+1);
				arr[x][y] = 0;
				row[x][i] = 0;
				col[y][i] = 0;
				squ[x/2*2+y/2][i] = 0;
			}
		}
	} else {
		sudoku(n+1);
	}
}
