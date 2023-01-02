#include <bits/stdc++.h>

using namespace std;

typedef struct child
{
    string name;
    int value;
} Child;

int main(int argc, char **argv)
{
    int n;
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    while (cin >> n, n)
    {
        vector<Child> children(n);
        for (int i = 0; i < n; i++)
        {
            Child temp;
            cin >> temp.name >> temp.value;
            children[i] = temp;
        }
        int step = children[0].value;
        int id = 0;
        while (children.size() > 1)
        {
            int step_mode = (children.size() == n ? step : step - 1) % children.size();
            if (step_mode < 0)
                step_mode += children.size();
            if (step & 1)
                id = (id + step_mode) % children.size();
            else
                id = (id + children.size() - step_mode) % children.size();
            step = children[id].value;
            children.erase(children.begin() + id);
            if ((step & 1) == 0)
                id = (id + children.size() - 1) % children.size();
        }
        cout << "Vencedor(a): " << children.back().name << endl;
    }

    return 0;
}