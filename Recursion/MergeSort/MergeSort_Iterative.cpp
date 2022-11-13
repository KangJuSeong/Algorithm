#include <iostream>
using namespace std;

void merge(int arr[], int low, int mid, int high, int *cnt);

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
		int k = 1;
		int j = 1;
		while (k < size) {
			for (int i=0; i<size; i+=j*2){
				if ((i+i+k)/2 >= size-1) break;
				merge(arr, i, (i+i+k)/2, i+k, &cnt);
			}
			k = k * 2 + 1;
			j = j * 2;
		}
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

