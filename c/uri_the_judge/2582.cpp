#include<iostream>

using namespace std;

int main(int argc, char **argv){
	int c,x,y;
	//ios_base::sync_with_stdio(false); cin.tie(false);
	cin >> c;
	string musicas [] = {"PROXYCITY", "P.Y.N.G.","DNSUEY!","SERVERS",
	"HOST!","CRIPTONIZE","OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"	};

	for (int i=0; i < c; i++){
		cin >> x >> y;
		cout << musicas[(x+y)] << endl;
	}
	return 0;
}

