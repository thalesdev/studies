#include <bits/stdc++.h>

using namespace std;

int bubble_sort(vector<int> vetor)
{
    int k, j, trocas = 0;

    for (k = 0; k < vetor.size() - 1; k++)
    {
        for (j = 0; j < vetor.size() - k - 1; j++)
        {
            if (vetor[j] > vetor[j + 1])
            {
                swap(vetor[j], vetor[j + 1]);
                trocas ++;
            }
        }
    }
    return trocas;
}

int main(int argc, char **argv)
{
    int n;
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int p;
        cin >> p;
        vector<int> values(p);
        for (int j = 0; j < p; j++)
        {
            cin >> values[j];
        }
        cout << "Optimal train swapping takes " << bubble_sort(values) << " swaps." << endl;
    }

    return 0;
}