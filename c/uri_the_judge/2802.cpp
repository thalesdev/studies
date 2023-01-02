#include<bits/stdc++.h>

using namespace std;

long long  comb( long long n, long long k )
{
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;

    long long result = n;
    for( long long i = 2; i <= k; ++i ) {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}

int main(int argc, char ** argv){
    int n;
    while (cin >> n){
        long long res = 1 + comb(n,4) + comb(n,2);
        cout << res << endl;
    }
    return 0;
}