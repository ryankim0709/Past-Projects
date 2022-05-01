#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int dmax;
int linesread;

int complexity(int depth) {
	int paths = 0;
	dmax = max(dmax, depth);
	while (true) {
		string a;
		getline(cin, a);
		linesread ++;
		if (a[0] == 'I' || a[0] == 'E') {
			paths ++;
		}
		else if (a[0] == '{') {
			int z = complexity(depth + 1);
			if (z == -1) {
				paths += 1;
				return paths;
			}
			paths +=  z - 1;
		}
		else if (a[0] == '}') {
			cout << paths << endl;
			if (paths == 0) {
				return -1;
			}
			return paths;
		}
	}
}

int main() {
	int cases;
	cin >> cases;
	for (int a=0; a<cases; a++) {
		int L, C, N;
		cin >> L >> C >> N;
		string temp;
		getline(cin, temp);
		dmax = 0;
		linesread = 0;
		int complex = 0;
		while (linesread < L) {
			complex += complexity(0);
		}
		if (complex == 0) {
			complex = 1;
		}
		cout << complex << " " << dmax << " ";
		if (complex <= C && dmax <= N) {
			cout << "PASS" << endl;
		}
		else {
			cout << "FAIL" << endl;
		}
	}
}