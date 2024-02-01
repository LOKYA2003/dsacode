#include <iostream>
using namespace std;

int BinarySearch(int arr[], int start, int end, int target)
{
    while (start <= end)
    {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] < target)
        {
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }

    return -1;
}

int main()
{

    int arr[8] = {1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8};

    int size = 8;
    int target = 7;
    int start = 0;
    int end = size - 1;
    int result = BinarySearch(arr, start, end, target);

    if (result == -1)
    {
        cout << "Element is not present in array";
    }
    else
    {
        cout << "Element is present at index " << result;
    }

    return 0;
}