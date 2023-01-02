#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(int argc, char **argv)
{
    cin.tie(0);
    int n;
    cin >> n;
    string temp_tree;
    getline(cin, temp_tree);
    map<string, int> trees;
    getline(cin, temp_tree);
    for (int i = 0; i < n; i++)
    {
        trees.clear();
        int total = 0;
        while (getline(cin, temp_tree))
        {
            if (temp_tree == "")
                break;
            if (trees.find(temp_tree) == trees.end())
            {
                trees[temp_tree] = 0;
            }
            trees[temp_tree]++;
            total++;
        }
        vector<string> keys;
        for (map<string, int>::iterator it = trees.begin(); it != trees.end(); ++it)
        {
            keys.push_back(it->first);
        }
        sort(keys.begin(), keys.end());
        for (const string& k : keys){
            cout << k << " "; 
            printf("%.4f\n",((float)trees[k]/(float)total)*100);
        }
        if (i < n-1)
            cout << endl;

    }
    return 0;
}