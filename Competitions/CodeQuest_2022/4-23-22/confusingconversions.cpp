#include <iostream>
#include <string>
using namespace std;

void formatHeight() {
	int X, Y;
	cin >> X >> Y;
	cout << X << '\'' << Y << '"' << endl;
}

void formatDate() {
	string y, m, d;
	cin >> y >> m >> d;
	while (y.length() < 4) {
		y = "0" + y;
	}
	while (m.length() < 2) {
		m = "0" + m;
	}
	while (d.length() < 2) {
		d = "0" + d;
	}
	cout << y << m << d << endl;
}

void concatenate() {
	string line;
	getline(cin, line);
	for (char a=1; a<line.length(); a++) {
		if (line[a] == ' ') {
			cout << ',';
		}
		else {
			cout << line[a];
		}
	}
	cout << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int a=0; a<cases; a++) {
		string function;
		cin >> function;
		if (function == "formatHeight") formatHeight();
		else if (function == "formatDate") formatDate();
		else concatenate();
	}
}