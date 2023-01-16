#include<iostream>
#include <algorithm>

using namespace std;
#define INF 99999999;
//각 정점마다 하나의 부모(parent) 정점으로 연결됨을 표시한다.
int visited[6];
int dist[6];

struct edge {
    int start;
    int end;
    int cost;
};

int main() {	//가중치의 합
	int answer = 0;

	//각 정점의 부모 정점을 본인으로 초기값 설정
	for (int i = 0; i < 6; i++) {
		visited[i] = 0;
        dist[i] = INF;
	}

	//edges.cost = 가중치
	//edges.start, edges.end = 간선으로 이어진 a,b 정점
	edge edges[20];
    int k = 0;
    for(int i=0;i<20;i=i+2) {
        int a, b, c;
        cin >> a >> b >> c;
        edges[i].cost = a;
        edges[i].start = b;
        edges[i].end = c;
        edges[i+1].cost = a;
        edges[i+1].start = c;
        edges[i+1].end = b;
    }
    dist[0] = 0;
    for(int i=0;i<6;i++) {
        int min_cost = INF;
        int min_idx = -1;
        for (int j=0;j<6; j++) {
            if(visited[j] != 1 && min_cost > dist[j]) {
                min_cost = dist[j];
                min_idx = j;
            } 
        }
        cout << min_cost << " " << min_idx << endl;
        if(min_idx < 0) continue;
        answer += min_cost;
        visited[min_idx] = 1;
        for(int j=0;j<20;j++) {
            if (edges[j].start == min_idx) {
                dist[edges[j].end] = min(dist[edges[j].end], edges[j].cost);
            }
        }
        for(int m=0; m<6;m++) {
            cout << " dist[" << m << "] : " <<  dist[m] << "      visited[" << m << "] : "<<  visited[m] << endl;  
        }
    }
    cout << "가중치 합 : " << answer;
	return 0;
}

	



