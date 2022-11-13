#include <iostream>
using namespace std;

void ExchangeCombi(int n, int k);

int coin[5] = {0, 1, 2, 5, 7};

int main(){
	ExchangeCombi(4, 20);
	return 0;
}

void ExchangeCombi(int n, int k) {
	int memo[11][10000]= {0};
	int i, j;
	memo[0][0] = 1;

	for(i=1;i<=n;i++){
		for(j=0;j<=k;j++) {
			if (j<coin[i]) {
				memo[i][j] = memo[i-1][j];
			} else {
				memo[i][j] = memo[i][j-coin[i]] + memo[i-1][j];
			}
		}

	}
	for(i=0;i<=n;i++) {
		for(j=0;j<=k;j++) {
			cout << memo[i][j] << " ";
		}
		cout << endl;
	}
}
