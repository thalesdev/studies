#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct dt
{
    char size;
    string name;
    string color;
} Data;

int int_size(char size)
{
    if (size == 'P')
        return 0;
    else if (size == 'M')
        return 1;
    return 2;
}

bool name_sort(Data a, Data b)
{
    return a.name < b.name;
}

int main(int argc, char **argv)
{
    int n, c = 0;
    while (cin >> n, n!=0)
    {
        c++;
        if (c > 1)
        {
            cout <<endl;
        }
        vector<Data> white_p, white_g, white_m, red_p, red_m, red_g;

        for (int i = 0; i < n; i++)
        {
            Data temp;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            getline(cin, temp.name);
            cin >> temp.color;
            cin.ignore(numeric_limits<streamsize>::max(), ' ');
            cin >> temp.size;
            int c = int_size(temp.size);
            vector<Data> *vet;
            if (temp.color == "branco")

            {
                vet = (c == 0) ? &white_p : (c == 1) ? &white_m : &white_g;
            }
            else
            {
                vet = (c == 0) ? &red_p : (c == 1) ? &red_m : &red_g;
            }
            vet->push_back(temp);
        }

        // White sorts

        sort(white_p.begin(), white_p.end(), name_sort);
        for (const Data &d : white_p)
            cout << d.color << " " << d.size << " " << d.name << endl;
        sort(white_m.begin(), white_m.end(), name_sort);
        for (const Data &d : white_m)
            cout << d.color << " " << d.size << " " << d.name << endl;
        sort(white_g.begin(), white_g.end(), name_sort);
        for (const Data &d : white_g)
            cout << d.color << " " << d.size << " " << d.name << endl;

        // Red sorts

        sort(red_p.begin(), red_p.end(), name_sort);
        for (const Data &d : red_p)
            cout << d.color << " " << d.size << " " << d.name << endl;
        sort(red_m.begin(), red_m.end(), name_sort);
        for (const Data &d : red_m)
            cout << d.color << " " << d.size << " " << d.name << endl;
        sort(red_g.begin(), red_g.end(), name_sort);
        for (const Data &d : red_g)
            cout << d.color << " " << d.size << " " << d.name << endl;
    }
}
