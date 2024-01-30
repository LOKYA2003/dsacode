#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i, j;

    bool swapped = true;
    for (i = 0; i < n - 1; i++)
    {

        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        if (swapped == false)
            break;
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{

    int arr[5] = {5,
                  43,
                  3,
                  24,
                  1};

    int n = 5;

    bubbleSort(arr, n);

    printArray(arr, n);
}
