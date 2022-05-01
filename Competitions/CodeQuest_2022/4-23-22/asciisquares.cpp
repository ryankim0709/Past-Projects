#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool checkstr(string a, int b) {
	if (b >= a.length()) return false;
	return a[b] == '_';
}

int main() {
	int cases;
	cin >> cases;
	for (int a=0; a<cases; a++) {
		int X;
		cin >> X;
		string temp;
		getline(cin, temp);
		string input[X];
		vector<bool> tiles[X];
		int maxwidth = 0;
		for (int b=0; b<X; b++) {
			getline(cin, input[b]);
			maxwidth = max(maxwidth, (int) input[b].length()/2);
			if (b != 0) {
				for (int c=0; c<input[b].length()-2; c+=2) {
					if (input[b][c] == '|' && input[b][c+1] == '_' && input[b][c+2] == '|' && checkstr(input[b-1], c+1)) {
						tiles[b].push_back(true);
					}
					else {
						tiles[b].push_back(false);
					}
				}
			}
		}
		int sum[X+1][maxwidth+1];
		for (int z=0; z<X; z++) {
			sum[z][0] = 0;
		}
		for (int y=0; y<maxwidth; y++) {
			sum[0][maxwidth] = 0;
		}
		for (int d=1; d<X+1; d++) {
			int e=1;
			for (; e<tiles[d].size()+1; e++) {
				sum[d][e] = tiles[d][e-1] + sum[d-1][e] + sum[d][e-1];
				cout << sum[d][e] << " ";
			}
			for (; e<maxwidth+1; e++) {
				sum[d][e] = sum[d-1][e] + sum[d][e-1];
				cout << sum[d][e] << " ";
			}
			cout << endl;
		}

		//check loop
		int squares = 0;
		for (int s=1; s<min(maxwidth, X); s++) {
			int threshold = s*s;
			for (int r=1; r<(X-s); r++) {
				for (int c=1; c<(X-s); c++) {
					if (sum[r+s][c+s] - sum[r+s][c-1] - sum[r-1][c+s] + sum[r-1][c-1] == threshold) squares ++;
				}
			}
		}
		cout << 'c' << endl;
		cout << squares << endl;
	}	
}