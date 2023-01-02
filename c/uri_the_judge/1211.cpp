#include <iostream>
#include <string>
#include <set>

using namespace std;

string max_substr_common(string one, string two){
        int  bg = 0;
        string aux;
        if (one.length() > two.length()){
            swap(one,two);
        }
        for (int i = 1; i <= one.length() - 1; i++){
            string sub =  one.substr(0,i);
            if (two.find(sub) != string::npos){
                if (sub.size() > bg){
                    bg = sub.size();
                    aux = sub;
                }
            }
        }
        return aux;
}



int main(int argc, char ** argv){
    int n;
    ios_base::sync_with_stdio(false); cin.tie(0);

    while(cin >> n){
        string numbers[n];
        set<string> prefix;
        for (int j = 0; j < n ; j++){
            cin >> numbers[j];
        } 
        int sump = 0;
        for(int xz=1; xz < n; xz++){
            for (int k=0; k < n; k++){
                if (k != xz){
                    string msubstr =  max_substr_common(numbers[k], numbers[xz]);
                    if(prefix.find(msubstr) == prefix.end()){
                        prefix.insert(msubstr);
                        sump+=msubstr.length();
                    }
                }
            }
        }
        cout << sump - 2 << endl;
    } 




}