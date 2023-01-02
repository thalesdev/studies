#include <iostream>
#include <string>

using namespace std;

int main(int argc, char ** argv){
    string a, b, aux;
    int bg ;
    while (getline(cin, a) && getline(cin, b)){
        bg = 0;
        if (a.length() > b.length()){
            swap(a,b);
        }
        for (int i = 0; i <= a.length() - 1; i++){
            for (int j = 1; j < a.length() - i + 1; j++){
                string sub =  a.substr(i,j);
                if (b.find(sub) != string::npos && sub != ""){
                    if (bg == 0)
                        aux = sub;
                    if (sub.size() > bg){
                        bg = sub.size();
                    }
                }
            }
        }
        cout << bg << endl;
    }


}