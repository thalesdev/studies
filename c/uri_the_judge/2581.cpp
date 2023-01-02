#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char **argv){
	int n;
	string str;
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> n;
	for(int i=0;i < n ;i++){
		cin >> str;
		cout << "I am Toorg!" << endl;
	}
	return 0;
}

