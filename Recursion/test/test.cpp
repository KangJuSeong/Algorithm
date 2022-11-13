#include <iostream>
using namespace std;

int coin[5] = {1, 5, 10, 21, 25};

coin
a[0] = 0;
a[1000] = {999999};
for i=0;i<n;i++
    for j=coin[i] j<=k;j++ {
        a[j] = min a[j] a[j-coin[i]] +1
    }


coin2
m[1000][1000] = {0}
m[0][0] = 1;
for i=0;i<n;i++
    for j=0;j<=k;j++{
        if(j < coin[i]) {
            m[i][j] = m[i-1][j]
        } else {
            m[i][j] = m[i][j-coin[i]] + m[i-1][j]
        }
    }


coeff
m[1000][1000] = {0}
for i=0;i<=n;i++
    for j=0;j<=k;j++ {
        if(i==j || j==0) {
            m[i]][j] = 1
        } else {
            m[i][j] = m[i-1][j-1] + m[i-1][j];
        }
    }

arr[i] > max1;
max1 = arr[i]
max2 = max1;

e;se if > max2
max2 = arr[i]

palindrome



