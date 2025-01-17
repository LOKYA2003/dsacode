
#include <iostream>
using namespace std;

//  selection sort algo

// [5,4,3,2,1]

void selectionSort(int arr[], int n)
{
    int i, j, index;

    // One by one move boundary of
    // unsorted subarray
    for (i = 0; i < n - 1; i++)
    {

        // Find the minimum element in
        // unsorted array
        index = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[index])
                index = j;
        }

        // Swap the found minimum element
        // with the first element
        if (index != i)
            swap(arr[index], arr[i]);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
        cout << endl;
    }
}

int main()
{

    int arr[5] = {5,
                  43,
                  3,
                  24,
                  1};

    int n = 5;

    selectionSort(arr, n);

    printArray(arr, n);
}