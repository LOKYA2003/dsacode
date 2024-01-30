#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    int i, j;
    // [3,2,1,4]
    // One by one move boundary of

    bool swapped = true; // Initialize swapped inside the outer loop
    for (i = 0; i < n - 1; i++)
    {

        for (j = 0; j < n - i - 1; j++) // Corrected the inner loop condition
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]); // Corrected the swap function
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
    cout << endl; // Move cout << endl; outside the loop to print the entire array on a new line
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
