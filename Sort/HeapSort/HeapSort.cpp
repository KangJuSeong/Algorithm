#include <iostream>
using namespace std;

int swp;
int heap[2002];
int heapSort(int n);
void fixHeap(int root, int k, int size);

void initHeap() {
	for(int i=0;i<2002;i++) {
		heap[i] = 0;
	}
}

int main() {
	int numTestCases, i, j;
	cin >> numTestCases;
	for(i=0;i<numTestCases;i++) {
		int n;
		cin >> n;
		initHeap();
		swp = 0;
		for(j=1;j<=n;j++) {
			cin >> heap[j];
		}
		cout << heapSort(n) << endl;
	}
	return 0;
}

int heapSort(int n) {
	int i;
	for(i=n/2;i>=1;i--) {
		fixHeap(i, heap[i], n);
	}
	for(i=n;i>=2;i--) {
		int m = heap[1];
		fixHeap(1, heap[i], i-1);
		heap[i] = m;
	}
	return swp;
}

void fixHeap(int root, int k, int n) {
	int vacant = root;
	int largerChild;

	while((heap[vacant*2]!=0 && vacant*2 <= n) || (heap[vacant*2+1]!=0 && vacant*2+1 <= n)){
		if(heap[vacant*2+1] != 0 && vacant*2+1 <= n) {
			// 두번 비교
			swp = swp + 2;
			if(heap[vacant*2] > heap[vacant*2+1]) {
				largerChild = vacant*2;
			} else {
				largerChild = vacant*2+1;
			}
		} else {
			// 한번 비교
			swp ++;
			largerChild = vacant*2;
		}
		if(k < heap[largerChild]) {
			heap[vacant] = heap[largerChild];
			vacant = largerChild;
		} else {
			break;
		}
	}
	heap[vacant] = k;
}

