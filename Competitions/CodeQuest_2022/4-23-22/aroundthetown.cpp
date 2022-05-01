#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

double distance(double x1, double y1, double x2, double y2) {
	return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

int main() {
	int cases;
	cin >> cases;
	for (int a=0; a<cases; a++) {
		int L, S;
		cin >> L >> S;
		vector<pair<double, double>> landmarks;
		vector<pair<double, double>> stops;
		for (int b=0; b<L; b++) {
			double c, d;
			cin >> c >> d;
			landmarks.insert({c, d});
		}
		for (int e=0; e<S; e++) {
			double f, g;
			cin >> f >> g;
			landmarks.insert({f, g});
		}
		
	}
}