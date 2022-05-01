#include <iostream>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
	int t;
	cin >> t;

	for (int a=0; a<t; a++) {
		int lines;
		cin >> lines;
		string temp;
		getline(cin, temp);

		map<int, int> letterfreqs;

		int totallength = 0;

		//gather word data
		for (int b=0; b<lines; b++) {
			string line;
			getline(cin, line);

			//analyze line
			int wordbuffer = 0;
			for (int c=0; c<line.length(); c++) {
				if ((int) line[c] >= 97 && line[c] <= 122) {
					letterfreqs[line[c]-97] ++;
					totallength ++;
				}
				else if ((int) line[c] >= 65 && line[c] <= 90) {
					letterfreqs[line[c]-65] ++;
					totallength ++;
				}
			}
		}

		cout << fixed << showpoint << setprecision(2);
		cout << totallength << endl;

		for (int c=0; c<26; c++) {
			cout << (char) (c+65) << ": ";
			cout << round((double) letterfreqs[c]/totallength*10000)/100 << "%" << endl;
		}
	}
}