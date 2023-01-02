#include <bits/stdc++.h>

using namespace std;


string combs[]{"BS","SB", "CF","FC"};

int main(int argc, char **c){

    ios_base::sync_with_stdio(false); cin.tie(0);
    string line;
    while(cin >> line){
        int count = 0;
        bool buffer = true;
        while(buffer){
            buffer = false;
            for(auto&& cb : combs){
                int id;
                if((id = line.find(cb)) == string::npos ) continue;
                string temp = line.substr(0,id) + line.substr(id+2);
                count ++;
                line = temp;
                buffer = true;
            }
        }
        cout << count << endl;
    }

    return 0;
}