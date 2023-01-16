#include <iostream>

using namespace std;

int a[101];
int dp[10001][10001];

void coin_2(int n, int k);
int main()
{
    int n, k;
    cin >> n;
    cin >> k;
    a[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    coin_2(n, k);
}

void coin_2(int n, int k)
{   
    for(int i = 1;i<=k;i++) {
        dp[0][i] = 0;
    }
    for(int i=0;i<=n;i++) {
        dp[i][0] = 1;
    }
    int num;
    for (int i = 1; i <=n; i++)
    {
        for(int j = 1; j<=k; j++) {
            if(j-a[i] < 0) { //[1, 2, 3, 4]
                num = 0;
            } else {
                num = dp[i][j-a[i]];
            }
            dp[i][j] = dp[i-1][j] + num;
            for(int l=0;l<=n;l++) {
                for(int q=0;q<=k;q++) {
                    cout << dp[l][q] << " ";
                }
                cout << endl;
            }
        }
    }
    cout << dp[n][k];
}