#include <iostream>
using namespace std;


int balancingScale(int arr[], int size);
int choiceWeight(int weight);
int chu[] = {100, 50, 20, 10, 5, 2 ,1};

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int j=0; j<numTestCases; j++) {
		int size;
		cin >> size;
		int arr[size];
		for (int i=0; i<size; i++) {
			cin >> arr[i];
		}
		int left = 0;
		int right = 0;
		cout << choiceWeight(balancingScale(arr, size)) << endl;
	}
	return 0;
}

int balancingScale(int arr[], int size) {
	int left = 0;
	int right = 0;
	for (int i=0; i<size; i++) {
		if (i==0 || left <= right) left += arr[i];
		else right += arr[i];
	}	
	int weight = left - right;
	if (weight < 0) weight *= -1;
	return weight;
}

int choiceWeight(int weight) {
	int cnt = 0;
	for (int i=0; i<7; i++) {
		int a = weight / chu[i];
		if (a == 0) continue;
		else {
			int b = weight % chu[i];
			weight = b;
			cnt += a;
		}
	}
	return cnt;
}
