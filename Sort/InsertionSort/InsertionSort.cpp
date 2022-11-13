#include <iostream>

#define MAX_SIZE 1000
void insertionSort(int a[], int n);


int main(){
	int numTestCases;
	scanf("%d", &numTestCases);
	for(int i=0; i<numTestCases; i++){
		int num;
		int a[MAX_SIZE];

		scanf("%d", &num);
		for (int j=0; j<num; j++){
			scanf("%d", &a[j]);
		}
		insertionSort(a, num);
		printf("\n");
	}
	return 0;
}

/* Insertion Sort 함수 */
void insertionSort(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;

	for (int i=1; i<n; i++){
		int tmp = a[i];
		int idx = -1;
		for (int j=i-1; j>=0; j--){
			countCmpOps ++;
			if (a[j]>tmp) {
				a[j+1] = a[j];
				countSwaps ++;
				idx = j;
			}
			else { break; }
		}
		if (idx != -1) { a[idx] = tmp; }
	}

	printf("%d %d", countCmpOps, countSwaps);
}
