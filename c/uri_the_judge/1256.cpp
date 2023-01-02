#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false); cin.tie(0);

    int n, m, c;
    cin >> n;
    for(int _=0; _<n; _++){
        cin >> m >> c;
        vector< vector<int> > hashmap(m);
        for(int i = 0; i < c; i++)
        {
            int temp;
            cin >> temp;
            hashmap[temp % m].push_back(temp);
        }
        for(int j=0; j < m; j++){
            cout << j <<" -> ";
            for (int& i: hashmap[j]){
                cout << i << " -> ";             }
            cout << "\\" << endl;
        }
        if (_ < n-1)
        cout << endl;
    }

    return 0;
}