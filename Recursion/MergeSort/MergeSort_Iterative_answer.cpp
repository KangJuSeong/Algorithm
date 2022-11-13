#include <iostream>
using namespace std;

void merge(int arr[], int low, int mid, int high, int *cnt);
void mergeSortIterative(int arr[], int n, int *cnt);

int main() {
	int numTestCases;
	cin >> numTestCases;
	for(int i=0; i<numTestCases; i++) {
		int size;
		cin >> size;
		int arr[size];
		for (int j=0; j<size; j++) {
			cin >> arr[j]; 
		}
		int cnt = 0;
		mergeSortIterative(arr, size, &cnt);
		cout << cnt << endl;
	}
	return 0;
}

void mergeSortIterative(int arr[], int n, int *cnt) {
	int size = 1;
	while (size < n) {
		for (int i=0; i<n; i+=2 *size) {
			int low = i;
			int mid = low + size - 1;
			int high = min(i+2*size-1, n-1);
			if (mid>=n-1) break;
			merge(arr, low, mid, high, cnt);
		}
		size *= 2;
	}
}

void merge(int arr[], int low, int mid, int high, int *cnt) {
	int i, j, k;
	int tmp[100];

	for(i=low; i<=high; i++) {
		tmp[i] = arr[i];
	}
	i = k = low;
	j = mid + 1;
	while(i<=mid && j<=high) {
		if (tmp[i] <= tmp[j]) {
			arr[k++] = tmp[i++];
		} else {
			arr[k++] = tmp[j++];
		}
		*cnt = *cnt + 1;
	}
	while (i<=mid) {
		arr[k++] = tmp[i++];
	}
	while(j<=high) {
		arr[k++] = tmp[j++];
	}
}

