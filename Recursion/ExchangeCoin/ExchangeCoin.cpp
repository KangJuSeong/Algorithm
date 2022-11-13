#include <iostream>
using namespace std;

int dp[1000];
int coin[4] = {1,2,3,7};

int main() {
	int i, j;
	for (i=1; i<=20; i++) {
		dp[i] = 999999999;
	}
	for (i=0; i<4;i++) {
		cout<< "동전 " << coin[i] << " 사용 시" << endl;
		for (j=coin[i]; j<=20; j++) {
			dp[j] = min(dp[j], dp[j-coin[i]]+1);	
			cout << "j : " << j << " " << "dp[j]: "<< dp[j] <<endl;
		}
	}
	cout << dp[20] << endl;
}