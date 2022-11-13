#include <iostream>
using namespace std;

int mcss(int arr[], int low, int high);

int main() {
	int numTestCases;
	cin >> numTestCases;

	for (int i=0; i<numTestCases; i++) {
		int arr[100];
		int size;
		cin >> size;
		for (int j=0; j<size; j++) {
			cin >> arr[j];
		}
		cout << mcss(arr, 0, size-1) << endl; 
	}
	return 0;
}

int mcss(int arr[], int low, int high) {
	if (low == high) return arr[low];

	int middle = (high + low) / 2;
	int left = -1001;
	int right = -1001;
	int sum = 0;

	for (int i=middle; i>=low; i--) {
		sum += arr[i];
		left = max(left, sum);
	}
	
	sum = 0;
	for (int i=middle+1; i<=high; i++) {
		sum += arr[i];
		right = max(right, sum);
	}

	int s = max(mcss(arr, low, middle), mcss(arr, middle+1, high));
	return max(left + right, s);
}
