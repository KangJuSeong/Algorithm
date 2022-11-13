#include <iostream>

#define MAX_SIZE 1000
void combSort(int a[], int n);


int main(){
	
	int numTestCases;
	scanf("%d", &numTestCases);

	for (int i=0; i<numTestCases; ++i){
		int num;
		int a[MAX_SIZE];

		scanf("%d", &num);
		for(int j=0; j<num; j++){
			scanf("%d", &a[j]);
		}
		combSort(a, num);
		printf("\n");
	}

	return 0;
}

void swap(int *a, int* b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

/* comb sort 함수 */
void combSort(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;
	float shrink = 1.3;
	bool sorted = false;
	int gap = n;

	while(sorted==false) {
		gap = gap / shrink;
		if(gap <= 1) {
			gap = 1;
			sorted = true;
		}
		
		int i = 0;
		while(i + gap < n) {
			countCmpOps ++;
			if(a[i] > a[i+gap]) {
				swap(&a[i], &a[i+gap]);
				sorted = false;
				countSwaps ++;
			}
			i ++;
		}
	}
	printf("%d %d ", countCmpOps, countSwaps);
}
