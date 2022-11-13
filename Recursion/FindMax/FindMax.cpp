#include <iostream>
using namespace std;

int findMax(int arr[], int low, int high, int size);

int main(){
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int arr[100];
		int size;
		cin >> size;
		for (int j=0;j<size;j++) {
			cin >> arr[j];
		}
		cout << findMax(arr, 0, size-1, size) << endl;
	}
	return 0;
}

int findMax(int arr[], int low, int high, int size) {
	if (size == 1) {
		return arr[low];
	}
	if (size == 2) {
		if (arr[low] > arr[high]) return arr[low];
		else return arr[high];
	} else {
		int offset = (low + high) / 2;
		int a = findMax(arr, low, offset, offset-low+1);
		int b = findMax(arr, offset+1, high, high-offset);
		if (a>b) return a;
		else return b;
	}
}
