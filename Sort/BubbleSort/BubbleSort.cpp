#include <iostream>

#define MAX_SIZE 1000
void bubbleSort(int a[], int n);
void bubbleSortImproved1(int a[], int n);
void bubbleSortImproved2(int a[], int n);
void copyArray(int a[], int b[], int n);

int main(){
	int numTestCases;
	int a[MAX_SIZE], b[MAX_SIZE];
	
	scanf("%d", &numTestCases);
	for (int i=0; i<numTestCases; ++i){
		int num;

		scanf("%d", &num);
		for (int j=0; j<num; j++){
			scanf("%d", &b[j]);
		}
		copyArray(a, b, num);
		bubbleSort(a, num);

		copyArray(a, b, num);
		bubbleSortImproved1(a, num);

		copyArray(a, b, num);
		bubbleSortImproved2(a, num);
		printf("\n");
	}
	return 0;
}

void swap(int* a, int* b){
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

/* BubbleSort 함수 */
void bubbleSort(int a[], int n){
	int countCmpOps = 0;  // 비교연산자 실행 횟수
	int countSwaps = 0;   // swap 함수 실행 횟수

	for(int i=0; i<n-1; i++){ 
		for(int j=0; j<n-i-1; j++){ 
			countCmpOps++;
			if(a[j] > a[j+1]){
				swap(&a[j], &a[j+1]);
				countSwaps++;	
			}
		}
	}
	printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 1 */
void bubbleSortImproved1(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;

	for(int i=0; i<n-1; i++){
		bool swapped = false;
		for(int j=0; j<n-i-1; j++){
			countCmpOps++;
			if(a[j] > a[j+1]){
				swap(&a[j], &a[j+1]);
				countSwaps++;
				swapped = true;
			}
		}
		if(swapped == false){
			break;
		}
	}
	printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 2 */
void bubbleSortImproved2(int a[], int n){
	int countCmpOps = 0;
	int countSwaps = 0;
	int lastSwappedPos = n;
	
	while(lastSwappedPos > 0){ 
		int swappedPos = 0;
		for(int j=0; j<lastSwappedPos-1; j++){ 
			countCmpOps++;
			if(a[j] > a[j+1]){
				swap(&a[j], &a[j+1]);
				swappedPos = j+1;
				countSwaps++;
			}
		}
		lastSwappedPos = swappedPos;
	}
	printf("%d %d ", countCmpOps, countSwaps);
}

void copyArray(int a[], int b[], int n){
	for (int i=0; i<n; i++){
		a[i] = b[i];
	}
}


