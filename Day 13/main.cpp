#include <iostream>
using namespace std;

int main()
{
    int arr[9] = {1,
                  3,
                  5,
                  5,
                  5,
                  5,
                  67,
                  123,
                  125};

    int size = 9;

    int start = 0;
    int end = size - 1;
    int target = 5;
    int last = -1;
    int first = -1;
    while (start <= end)
    {

        int mid = (start + end) / 2;

        if (arr[mid] == target)
        {
            first = mid;

            return mid;
        }
        else if (arr[mid] < target)
        {
            last = mid;

            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }

    cout << first << endl;
    cout << last << endl;
}