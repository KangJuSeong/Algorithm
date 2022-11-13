#include <iostream>
using namespace std;

void mcssKadane(int arr[], int size);

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
		mcssKadane(arr, size); 
	}
	return 0;
}

void mcssKadane(int arr[], int size) {
	int start = 0;
	int end = 0;
	int rstart = 0;
	int m[size];
	m[0] = arr[0];
	int max_val = m[0];
	for (int i=1; i<size; i++) {
		int target;
		int section = m[i-1] + arr[i];
		if (section >= arr[i]) {
			m[i] = section;
			target = section;
		} else {
			if (arr[i] == 0) {
				m[i] = section;
				continue;
			}
			m[i] = arr[i];
			rstart = i;
			target = arr[i];
		}
		if (target > max_val) {
			start = rstart;
			end = i;
			max_val = target;
		}
	}
	if (max_val < 0) {
		max_val = 0;
		start = -1;
		end = -1;
	}
	cout << max_val << " " << start << " " << end << endl;
}
