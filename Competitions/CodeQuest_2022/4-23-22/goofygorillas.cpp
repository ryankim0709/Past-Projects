#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int a=0; a<t; a++) {
		string c, d;
		cin >> c >> d;
		if (c == d) {
			cout << "true" << endl;
		}
		else {
			cout << "false" << endl;
		}
	}
}