#include <iostream>
using namespace std;

int max1=0;
int max2=0;

void fn(int arr[], int low, int high) {
    if (high==low) {
        if (arr[high] > max1) {
            max2 = max1;
            max1 = arr[high];
        } else if (arr[high] > max2) {
            max2 = arr[high];
        }
    } else {
        int mid = (low + high)/2;
        fn(arr, low, mid);
        fn(arr, mid+1, high);
    }
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
        fn(arr, 0, n-1);
        cout << max2 << endl;
        max1=0;
        max2=0;
    }
    return 0;
}