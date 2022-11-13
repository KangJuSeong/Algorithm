#include <iostream>
using namespace std;

int fn(int arr[], int low, int high) {
    if ((high-low+1) < 2) return 1;
    if (arr[low] != arr[high]) return 0;
    return fn(arr, low+1, high-1);
}

int main() {
    int test;
    cin >> test;
    for(int i=0;i<test;i++) {
        int n;
        cin >> n;
        int arr[n];
        for(int j=0;j<n;j++) {
            cin >> arr[j];
        }
        cout << fn(arr, 0, n-1) << endl;
    }
}