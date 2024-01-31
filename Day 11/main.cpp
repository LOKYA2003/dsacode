
#include <iostream>
using namespace std;

// Example
// arr[]: {12, 11, 13, 5, 6}

void insertSort(int arr[], int size)
{

    for (int i = 1; i < size; i++)
    {

        for (int j = i; j > 0; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                swap(arr[j], arr[j - 1]);
            }
            else
            {
                break;
            }
        }
    }
}

void printArr(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{

    int arr[5] = {12,
                  11,
                  1323,
                  5,
                  6};

    int size = 5;
    insertSort(arr, size);
    printArr(arr, size);
}