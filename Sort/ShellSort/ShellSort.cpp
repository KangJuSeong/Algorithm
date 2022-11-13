#include <iostream>

#define MAX_SIZE 1000
void shellSort(int a[], int n);


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
		shellSort(a, num);
		printf("\n");
	}
	return 0;
}

/* Shell Sort 함수 */
void shellSort(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;
	int shrinkRatio = 2;
	int gap = n / shrinkRatio;

	while (gap>0) {
		for (int i=gap; i<n; i++) {
			int tmp = a[i];
			int idx = -1;
			for (int j=i; j>=gap; j-=gap){
				countCmpOps ++;
				if(a[j-gap] > tmp) {
					a[j] = a[j-gap];
					countSwaps ++;
					idx = j-gap;
				}
				else { break; }
			}
			if (idx != -1) { 
				a[idx] = tmp; 
			}
		}
		gap /= shrinkRatio;
	}
	printf("%d %d", countCmpOps, countSwaps);
}
