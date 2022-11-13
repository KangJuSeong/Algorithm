#include <iostream>
using namespace std;

void merge(int arr[], int low, int mid, int high, int *cnt);
void divide(int arr[], int low, int mid, int high, int *cnt);

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
		divide(arr, 0, (size-1)/2, size-1, &cnt);
		merge(arr, 0, (size-1)/2, size-1, &cnt);
		cout << cnt << endl;
	}
	return 0;
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

void divide(int arr[], int low, int mid, int high, int *cnt) {
	if (low == mid) {
		return ;
	} else {
		divide(arr, low, (low+mid)/2, mid, cnt);
		cout << low << " " << mid << endl;
		merge(arr, low, (low+mid)/2, mid, cnt);
		divide(arr, mid+1, (mid+1+high)/2, high, cnt);
		cout << mid+1 << " " << high << endl;
		merge(arr, mid+1, (mid+high+1)/2, high, cnt);
	}
}



