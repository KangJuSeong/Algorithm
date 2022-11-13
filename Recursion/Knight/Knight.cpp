#include <iostream>
using namespace std;

#define MAXSIZE 9
#define MARK 1
#define UNMARK 0

typedef struct Point {
	int x, y;
} point;
int board[MAXSIZE][MAXSIZE];
int path[MAXSIZE][MAXSIZE];
point direction[8] = {{1, -2}, {2, -1}, {2, 1}, {1, 2},
						{-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}};
int knightTour(int m, int n, point pos, int counter);

int main() {
	int numTestCases;
	cin >> numTestCases;
	for (int k=0; k<numTestCases; k++) {
		point start;
		int m, n;
		cin >> m >> n >> start.y >> start.x;
		for(int i=1; i<=m;i++) {
			for(int j=1;j<=n;j++) {
				board[i][j] = UNMARK;
			}
		}
		board[start.y][start.x] = MARK;
		path[start.y][start.x] = 1;
		if (knightTour(m, n, start, 1)) {
			cout << 1 << endl;
			for (int i=1; i<=m; i++) {
				for (int j=1;j<=n;j++) {
					cout << path[i][j] << " ";
				}
				cout << endl;
			}
		}
		else {
			cout << 0 << endl;
		}
	}
	return 1;
}

int knightTour(int m, int n, point pos, int counter) {
	point next;

	if (counter == m*n) {
		return 1;
	}
	for (int i=0; i<8; i++) {
		next.x = pos.x + direction[i].x;
		next.y = pos.y + direction[i].y;

		if (next.x > 0 && next.x <= n &&
			next.y > 0 && next.y <= m &&
			board[next.y][next.x] != MARK) {
			board[next.y][next.x] = MARK;
			path[next.y][next.x] = counter + 1;
			if (knightTour(m, n, next, counter + 1)) {
				return 1;
			}
			board[next.y][next.x] = UNMARK;
		}
	}
	return 0;
}



