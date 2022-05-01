#include <iostream>
using namespace std;

int main() {
	int words;
	cin >> words;
	for (int a=0; a<words; a++) {
		string b;
		cin >> b;
		int clicks = 0;
		for (int c=0; c<b.length(); c++) {
			clicks += (int) b[c] - 96;
		}
		cout << clicks << endl;
	}
}