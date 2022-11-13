#include <iostream>
using namespace std;

int partition_romuto(int arr[], int low, int high, int *sp, int *cnt);
int partition_hoare(int arr[], int low, int high, int *sp, int *cnt);
void quicksort_hoare(int arr[], int low, int high, int *sp, int *cnt);
void quicksort_romuto(int arr[], int low, int high, int *sp, int *cnt);

int main() {
	int numTestCses;
	cin >> numTestCses;
	for (int i=0; i<numTestCses; i++) {
		int size;
		cin >> size;
		int romuto_arr[size];
		int hoare_arr[size];
		int hoare_swap = 0;
		int romuto_swap = 0;
		int hoare_cnt = 0;
		int romuto_cnt = 0;
		for (int j=0; j<size; j++) {
			int h;
			cin >> h;
			romuto_arr[j] = h;
			hoare_arr[j] = h;
		}
		quicksort_hoare(hoare_arr, 0, size-1, &hoare_swap, &hoare_cnt);
		quicksort_romuto(romuto_arr, 0, size-1, &romuto_swap, &romuto_cnt);
		cout << hoare_swap << " " << romuto_swap << " " << hoare_cnt << " " << romuto_cnt << endl;
	}

	return 0;
}

void quicksort_hoare(int arr[], int low, int high, int *sp, int *cnt) {
	if ((high-low) <= 0) {
		return ;
	} else {
		int j = partition_hoare(arr, low, high, sp, cnt);
		quicksort_hoare(arr, low, j, sp, cnt);
		quicksort_hoare(arr, j+1, high, sp, cnt);
	}
}

void quicksort_romuto(int arr[], int low, int high, int *sp, int *cnt) {
	if ((high-low) <= 0) {
		return ;
	} else {
		int j = partition_romuto(arr, low, high, sp, cnt);
		quicksort_romuto(arr, low, j-1, sp, cnt);
		quicksort_romuto(arr, j+1, high, sp, cnt);
	}
}


int partition_romuto(int arr[], int low, int high, int *sp, int *cnt) {
	int pivot = arr[low];
	int j = low;
	for (int i=j+1; i<=high; i++) {
		*cnt = *cnt + 1;
		if (arr[i] < pivot) {
			j ++;
			swap(arr[i], arr[j]);
			*sp = *sp + 1;
		}
	}
	swap(arr[j], arr[low]);
	*sp = *sp + 1;
	return j;
}

int partition_hoare(int arr[], int low, int high, int *sp, int *cnt) {
	int pivot = arr[low];
	int i = low - 1;
	int j = high + 1;
	while (true) {
		*cnt = *cnt + 1;
		while (i < high && arr[++i] < pivot) {
			*cnt = *cnt + 1; 
		}
		*cnt = *cnt + 1;
		while (j > low && arr[--j] > pivot) {
			*cnt = *cnt + 1; 
		}
		if (j > i) {
			swap(arr[j], arr[i]);
			*sp = *sp + 1;
		} else return j;
	}
}
