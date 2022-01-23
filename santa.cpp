#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long solve(vector<long long> toys, int n)
{
    long long res = 0;
    for (int i = 0; i < n; i++)
    {

        if (n - i >= 5)
        {
            auto min = *min_element(toys.begin() + i, toys.end() + i + 5);
            res += min;
        }else{
            break;
        }
    }

    return res;
}

int main()
{

    vector<long long> toys;
    int n;
    cin >> n;
    for (int i = 0, x; i < n; i++)
    {
        cin >> x;
        toys.push_back(x);
    }

    cout << solve(toys, n) << endl;
}