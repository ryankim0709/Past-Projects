#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int a=0; a<cases; a++) {
		int doors, rounds, opened;
		cin >> doors >> rounds >> opened;
		double percent = 0;
		double last;
		//Initial Guess
		last = 1.0/doors;
		percent += last;
		doors --;
		for (int b=0; b<rounds; b++) {
			doors -= opened;
			last = (1.0-percent)/doors;
			percent += last;
			doors --;
		}
		cout << fixed << showpoint << setprecision(2);
		cout << last*100 << '%' << endl;
	}
}