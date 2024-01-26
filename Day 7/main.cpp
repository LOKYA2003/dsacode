#include <iostream>
using namespace std;

// Traverse array
// Linear Search
// Reverse Array
// Second maximum array in array

int secondLargest(int arr[], int size)
{

    // 1. largest
    // 2. secondL
    int largest = INT8_MIN;
    int secondL = -1;
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > arr[largest])
            largest = i;
    }
    for (int i = 0; i < size; i++)
    {

        if (arr[i] != largest)
        {
            if (secondL == -1)
            {
                secondL = i;
            }
            else if (arr[i] > arr[secondL])
            {
                secondL = i;
            }
        }
    }

    return secondL;
}

int main()
{
    int arr[5] = {23,
                  43,
                  22,
                  11,
                  4};
    int size = 5;

    int secondL = secondLargest(arr, size);

    cout << secondL;
}
