#include<bits/stdc++.h>

using namespace std;


bool *SieveOfEratosthenes(long long n) 
{ 
    bool *prime = (bool*)malloc(sizeof(bool)*(n+1)); 
    memset(prime, true, sizeof(bool)*(n+1)); 
    for (long long p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        { 
            for (long long i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
    return prime;
}

int main(int argc, char** argv){
    unsigned long long n;
    bool *primes = SieveOfEratosthenes(1000000);
    while(cin >> n && n != 0){
        unsigned long long n_ = n;
        unsigned long long vp[] = {0,0};
        unsigned long long lp = 2;
        int c=0;
        unsigned long long vi = n < 1000000 ? n : 1000000;
        while (1){
            bool err = true;
            for(unsigned long long i =lp+1; i< vi; i++){
                if (primes[i]  && n%i == 0){
                    n/= i;
                    vp[c] = i;
                    lp = i;
                    err = false;
                    c++;
                }
            }
            if (err){
                vi = (unsigned long long)sqrt(n);
                primes = SieveOfEratosthenes(vi);
            }
            if(c == 2 | n == 1){
                break;
            }
        }
        unsigned long long llp = (unsigned long long)(n_/(vp[0]*vp[1]));
        cout << n_ << " = " << vp[0] << " x " << vp[1] << " x " << llp << endl;
    }
    return 0;
}