#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int mode;

int sorter(int a, int b)
{
    int M = ::mode, m = ::mode;
    int mda = a%m, mdb = b%m;
    if (mda == mdb){ 
        if(abs(a)%2 ==abs(b)%2){
            return ((a%2) & 1) ? (a > b) : (b > a);
        }
        return abs(a)%2 > abs(b)%2;
    }
    return mda < mdb;
}

int main(int argc, char **argv)
{
    int n, m;
    while (cin >> n >> ::mode, n != 0 && ::mode != 0)
    {
        vector<int> values;
        for (int i = 0; i < n; i++)
        {
            int temp;
            cin >> temp;
            values.push_back(temp);
        }
        sort(values.begin(), values.end(), sorter);
        cout << n << " " << ::mode << endl;
        for (const int &i : values)
            cout << i << endl;
    }

    cout << "0 0" << endl;
}
