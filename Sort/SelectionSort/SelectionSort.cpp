#include <iostream>

#define MAX_SIZE 1000
void selectionSort(int a[], int n);


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
		selectionSort(a, num);
		printf("\n");
	}

	return 0;
}

void swap(int *a, int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

/* Selection Sort 함수 */
void selectionSort(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;

	for (int i=0; i<n-1; i++) {
		int _min = i;
		for(int j=i+1; j<n; j++) {
			countCmpOps ++;
			if (a[j] < a[_min]){
				_min = j;
			}
		}
		if (_min != i) {
			swap(&a[_min], &a[i]); 
			countSwaps ++;
		}
	}

	printf("%d %d", countCmpOps, countSwaps);
}
