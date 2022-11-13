#include <iostream>
using namespace std;

int binarySearch(int arr[], int target, int low, int high);

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; i++) {
		int high, target;
		cin >> high;
		cin >> target;
		int arr[high];
		for (int j=0; j<high; j++) {
			cin >> arr[j];
		}		
      	cout << binarySearch(arr, target, 0, high-1) << endl;
	}
 
	return 0;
}


int binarySearch(int arr[], int target, int low, int high) {
	if ((low-high) >= 0) {
		if (target == arr[low]) return low;
		else return -1;
	} else {
		int middle = (low + high) / 2;
		if (target < arr[middle]) {
			return binarySearch(arr, target, low, middle-1);
		} else if (target > arr[middle]) {
			return binarySearch(arr, target, middle+1, high);
		} else {
			return middle;
		}
	}
}
