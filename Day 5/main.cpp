
#include <iostream>
using namespace std;

// Arrays

// 1. Find the largest number in array

int findLargest(int arr[], int size)
{
    int largest = 0;
    // 1. 0 < 11 = 11
    // 2. 11 < 2 - NO
    // 3. 11 < 3 - NO
    // 4. 11 < 43 - 43
    // 5. 43 < 5 - No

    for (int i = 0; i < size; i++)
    {
        if (largest < arr[i])
        {
            largest = arr[i];
        }
    }

    return largest;
}

int findSmallest(int arr[], int size)
{
    int smallest = INT8_MAX;
    // 1. 0 < 11 = 11
    // 2. 11 < 2 - NO
    // 3. 11 < 3 - NO
    // 4. 11 < 43 - 43
    // 5. 43 < 5 - No

    for (int i = 0; i < size; i++)
    {
        if (smallest > arr[i])
        {
            smallest = arr[i];
        }
    }

    return smallest;
}
int main()
{

    int arr[5] = {11,
                  2,
                  3,
                  43,
                  5};
    int size = 5;

    int largestElement = findLargest(arr, size);

    cout << "The arrays largest element is " << largestElement << endl;

    int smallestElement = findSmallest(arr, size);

    cout << "The arrays smallest element is " << smallestElement << endl;
}